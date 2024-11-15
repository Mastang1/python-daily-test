import os, sys, time
from abc import ABC, abstractproperty, abstractmethod


class TcfTestBase(ABC):
    def __init__(self):
        self._srcCode = """
None
"""

    @abstractproperty
    def sourceCode(self):
        pass

    def __enter__(self):
        print("Entry".center(9, "*"))
    """
    exception: 异常
    exception_type : 异常类型
    exception_value : 异常的值（原因）
    exception_traceback : 异常发生的位置（回溯、追溯）
    """
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class TcfTest(TcfTestBase):
    @abstractproperty
    def setsss(self):
        pass




class InstruBase(ABC):
    """
    Display 
    """
    def __init__(self):
        pass

    @abstractproperty
    def setsss(self):
        pass

    @abstractmethod
    def methoda(self):
        pass

if __name__ == "__main__":
    pass