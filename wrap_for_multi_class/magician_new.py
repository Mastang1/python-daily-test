from functools import wraps
import sys
import io
from multiprocessing.managers import BaseManager

class TestClass:
    def tcf_method00(self):
        print("tcf_method called")

    def tcf_method01(self):
        print("tcf_method01 called")

    def tcf_method02(self):
        print("tcf_method02 called")

class DualStdout:
    def __init__(self):
        self.console = sys.stdout
        self.stream = io.StringIO()

    def write(self, message):
        self.console.write(message)
        self.stream.write(message)

    def flush(self):
        self.console.flush()
        self.stream.flush()

    def getvalue(self):
        return self.stream.getvalue()

class DualStderr:
    def __init__(self):
        self.console = sys.stderr
        self.stream = io.StringIO()

    def write(self, message):
        self.console.write(message)
        self.stream.write(message)

    def flush(self):
        self.console.flush()
        self.stream.flush()

    def getvalue(self):
        return self.stream.getvalue()

# 在模块级别定义包装类，避免序列化问题
class WrappedTestClass(TestClass):
    pass

class Magician:
    @staticmethod
    def wrap_methods_with_hooks(paramClass, wrapped_class, method_prefix='tcf', pre_hook=None, post_hook=None):
        if pre_hook is None or post_hook is None:
            raise ValueError("pre_hook and post_hook must be provided")
        
        # 遍历原始类的所有方法
        for name, method in vars(paramClass).items():
            if callable(method) and name.startswith(method_prefix):
                original_method = method
                
                # 使用闭包捕获当前方法
                def create_wrapper(original):
                    @wraps(original)
                    def wrapper(self, *args, **kwargs):
                        # 执行前置钩子
                        pre_hook_result = pre_hook()
                        # 执行原始方法
                        method_result = original(self, *args, **kwargs)
                        # 执行后置钩子
                        post_hook_result = post_hook()
                        # 返回结构化结果
                        return {
                            'method_result': method_result,
                            'pre_hook_result': pre_hook_result,
                            'post_hook_result': post_hook_result
                        }
                    return wrapper
                
                # 将包装后的方法设置到新类上
                setattr(wrapped_class, name, create_wrapper(original_method))
        
        return wrapped_class
    
    @staticmethod
    def pre_hook():
        print("pre_hook called")

    @staticmethod
    def post_hook():
        print("post_hook called")

    @staticmethod
    def pre_redirect_std():
        sys.stdout = DualStdout()
        sys.stderr = DualStderr()

    @staticmethod
    def post_redirect_std():
        ret_info = sys.stdout.getvalue().strip()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        return ret_info

class TestClassManager(BaseManager):
    pass

def get_wrapped_class():
    """返回包装后的类，确保在子进程中也能使用"""
    return Magician.wrap_methods_with_hooks(TestClass, WrappedTestClass, pre_hook=Magician.pre_redirect_std, post_hook=Magician.post_redirect_std)

if __name__ == "__main__":
    # 获取包装后的类
    WrappedTestClass = get_wrapped_class()
    
    # 注册包装后的类而不是原始类
    TestClassManager.register('TestClass', WrappedTestClass)
    test_class_manager = TestClassManager()
    test_class_manager.start()
    
    result = test_class_manager.TestClass().tcf_method01()
    print(result, "\n\n")