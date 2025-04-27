
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
