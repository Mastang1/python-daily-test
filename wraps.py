from functools import wraps


def log_io(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 打印输入参数
        print(f"调用函数: {func.__name__}")
        
        # 执行原函数
        result = func(*args, **kwargs)
        
        # 打印输出结果
        print(f"返回结果: {result}")
        return result
        
    return wrapper



class TestSuite:
    @log_io
    def testcase01(self):
        """
        doc:testcase01
        """
        print("testcase01")
    @log_io
    def testcase02(self):
        """
        doc:testcase02
        """
        print("testcase02")
    @log_io
    def testcase03(self):
        """
        doc:testcase03
        """
        print("testcase03")

if __name__ == "__main__":
    suite = TestSuite()
    for name in suite.__class__.__dict__:
        if name.startswith("testcase"):
            testcase = getattr(suite, name)
            print(testcase.__doc__)