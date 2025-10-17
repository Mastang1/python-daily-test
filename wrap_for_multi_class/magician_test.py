from functools import wraps
import sys
import io

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

class Magician:
    @staticmethod
    def wrap_methods_with_hooks(paramClass, method_prefix='tcf', pre_hook=None, post_hook=None):

        if pre_hook is None or post_hook is None:
            raise ValueError("pre_hook and post_hook must be provided")
            
        for name, method in vars(paramClass).items():
            if callable(method) and name.startswith(method_prefix):
                original_method = method
                
                # 使用闭包捕获当前方法
                def create_wrapper(original):
                    @wraps(original)
                    def wrapper(*args, **kwargs):
                        # 执行前置钩子
                        pre_hook_result = pre_hook()
                        # 执行原始方法
                        method_result = original(*args, **kwargs)
                        # 执行后置钩子
                        post_hook_result = post_hook()
                        # 返回结构化结果
                        return {
                            'method_result': method_result,
                            'pre_hook_result': pre_hook_result,
                            'post_hook_result': post_hook_result
                        }
                    return wrapper
                
                setattr(paramClass, name, create_wrapper(original_method))
        
        return paramClass
    
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

if __name__ == "__main__":
    # 应用装饰器
    # Magician.wrap_methods_with_hooks(TestClass, pre_hook=Magician.pre_hook, post_hook=Magician.post_hook)
    Magician.wrap_methods_with_hooks(TestClass, pre_hook=Magician.pre_redirect_std, post_hook=Magician.post_redirect_std)
    # 创建实例
    test_instance = TestClass()
    
    # 调用被装饰的方法
    result = test_instance.tcf_method01()
    print(result, "\n\n")

    result = test_instance.tcf_method02()
    print(result, "\n\n")

    result = test_instance.tcf_method00()
    print(result, "\n\n")