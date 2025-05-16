
gl_variable = "Today is a good day."

class Presenter:
    def __init__(self, show_choices):  # 接收装饰器参数
        self.show_choices = show_choices
        
    def __call__(self, func):   # 接收被装饰函数
        def wrapper(*args, **kwargs):
            if self.show_choices == "#param":
                result = func(*args, **kwargs)
                self.__show_param(func)
                return result
            elif self.show_choices == "#result":
                result = func(*args, **kwargs)
                self.__show_result(result)
                return result
            else:
                print("no choice")
                return func(*args, **kwargs)
        return wrapper

    def __show_param(self, func: callable):
        print(func.__code__.co_varnames)
        print(gl_variable)

    def __show_result(self, result):
        print(result)
        print(gl_variable)


class TcsInstru(object):
    @Presenter("#param")
    def init(self, a, b):
        return a + b

    @Presenter("#param")
    def open(self):
        return "open"
    
    @Presenter("#result")
    def read(self):
        return[1,2, "one", "two"]

    def write(self, data):
        return "write"

    def close(self):
        return "close"

    def deinit(self):
        return "deinit"

class TestTask:
    def testcase01(self):
        device = TcsInstru()
        device.init(1, 2)
        device.open()
        device.read()

    def testcase0(self):
        device = TcsInstru()
        device.init(1, 2)
        device.open()
        device.read()

if __name__ == '__main__':
    test_class = TcsInstru()
    foo = test_class.init
    foo(1, 2)
    print("*" * 10)
    gl_variable = "Hello, World!"
    foo(3, 4)
"""
#python 有没有方法可以通过操作类或者对象，为每个对象的成员添加装饰器
 #类装饰器
def log_io(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用方法: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"返回结果: {result}")
        return result
    return wrapper

def decorate_all_methods(cls):
    for name, method in vars(cls).items():
        if callable(method) and not name.startswith('__'):
            setattr(cls, name, log_io(method))
    return cls

@decorate_all_methods
class MyClass:
    def method1(self):
        return "方法1"
    
    def method2(self):
        return "方法2"
    
#元类装饰器
class LoggingMeta(type):
    def __new__(cls, name, bases, namespace):
        for attr_name, attr_value in namespace.items():
            if callable(attr_value) and not attr_name.startswith('__'):
                namespace[attr_name] = log_io(attr_value)
        return super().__new__(cls, name, bases, namespace)

class MyClass(metaclass=LoggingMeta):
    def method1(self):
        return "方法1"
    
    def method2(self):
        return "方法2"

#运行时添加
class MyClass:
    def method1(self):
        return "方法1"
    
    def method2(self):
        return "方法2"

# 创建实例后动态装饰
obj = MyClass()
for name in dir(obj):
    if not name.startswith('__'):
        attr = getattr(obj, name)
        if callable(attr):
            setattr(obj, name, log_io(attr))

"""