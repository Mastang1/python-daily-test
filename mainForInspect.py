import functools
import inspect

def log_function_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"当前函数名: {inspectest_func.currentframe().f_code.co_name}")
        return func(*args, **kwargs)
    return wrapper
 
@log_function_name
def my_func():
    pass

# today 
def test_func(param = 'Today'):
    strFirst = 'Today is a nice day.'
    '''
    nice day
    '''
    print(inspect.currentframe().f_code.co_name)
    
class AAA:
    '''
    AAA name etc.
    '''
    def __init__(self):
        self.param = 'nice day.'
        self.list = ['a', 'b', 1, 4, 5]
    def myMethod(self):
        self.param2 = None
        return 'base'
    def getInst(self):
        self.tang = 'tangyapeng'
        return self
    
class BBB(AAA):
    Bparam = 'dadada'

    def myMethod(self):
        def foo1():
            print(inspect.currentframe().f_code.co_name)
        def foo2():
            print(inspect.currentframe().f_code.co_name)
        def foo():
            foo1()
            foo2()
        foo()
if __name__ == '__main__':
    '''
    the method of class and instance is different.*****************
    '''
    #  print(test_func.__name__, test_func.__doc__, test_func.__code__, test_func.__defaults__)
    # test_func()
    # print(test_func.__defaults__,'  and ', test_func.__kwdefaults__, inspect.isabstract(test_func))


    # aaa=AAA()
    # aaa.getInst().myMethod()
    # for it in aaa.__dict__:
    #     print(str(it), type(getattr(aaa, it)))
    #     if isinstance(getattr(aaa, it),list):
    #         print(getattr(aaa, it))
    bbb = BBB()
    bbb.myMethod()