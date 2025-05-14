import os, sys, time
from functools import wraps
"""
This function is as the part of the test runner, it will be used to log the test case.
And, the can design different runner to run the test case.
"""

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


def foo():
    print("foo")

listFuncs = []
listVariantFuncs = []
listFuncs.append(foo)

for func in listFuncs:
    @log_io
    def variant_foo():
        func()
    listVariantFuncs.append(variant_foo)

for variant_foo in listVariantFuncs:
    variant_foo()