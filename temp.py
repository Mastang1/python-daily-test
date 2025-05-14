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