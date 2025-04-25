
gl_string = "hello world"

def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"调用函数 {func.__name__}，参数:")
        if args:
            print("位置参数:", args)
        if kwargs:
            print("关键字参数:", kwargs)
        args[0].display_input()
        return func(*args, **kwargs)
    return wrapper


class FrontEnd():

    def display_input(self):
        print("display_input {}".format(gl_string))

    def display_output(self):
        print("display_output {}".format(gl_string))

class TcsInstru(FrontEnd):

    @log_args
    def test_add(self, a, b):
        return a + b

    def hello(self):
        print("hello")


class TestTask():
    def testcase_01(self):
        print("testcase_01")



if __name__ == '__main__':
    test_class = TcsInstru()
    foo = test_class.test_add
    foo(1, 2)
    print("#"*80)
    gl_string = "today is nice day"
    foo(1, 2)
