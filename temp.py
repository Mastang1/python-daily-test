import os, sys, time
import stub_subclass

def test(arg1: int, arg2: str = "default", arg3: float = 3.14) -> bool:
    """
    This is a test function.
    """
    return True



# 输出: [<class '__main__.ChildClass1'>, <class '__main__.ChildClass2'>]
def test_find_subclass():
    print(stub_subclass.BaseClass.__subclasses__()) 

if __name__ == "__main__":
    # print(test.__doc__)
    # print(test.__name__, test.__annotations__)
    test_find_subclass()