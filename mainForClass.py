import inspect
 
class A:
    def method_a(self):
        pass
 
class B(A):
    def method_b(self):
        pass
 
class C(B):
    def method_c(self):
        pass
 



def list_methods(cls):
    # 遍历类以及所有父类中的所有方法
    methods = [func for func in cls.__dict__.values() if inspect.isfunction(func)]
    return methods
 
class TYP:
    def __init__(self, name = 'testFunc'):
        self.funcName = name
    def method_a(self):
        print("122222")
    def method_b(self):
        print(" -- method_b")
    def method_c(self):
        print(" -- method_c")
    def method_d(self):
        print(" -- method_d")


# 使用示例


if __name__ == '__main__':
    # print(TYP.__dict__)
    typ = TYP()
    # curMethod = getattr(typ, 'method_a', None)
    # print(curMethod('uuuuuu'))
    for it in type(typ).__dict__:
        if str(it).startswith('method'):
            method = getattr(typ, str(it), None)
            result = method()
    # tmpTest = TYP('method_b')
    # curMethod = getattr(tmpTest, tmpTest.funcName, None)
    # curMethod()