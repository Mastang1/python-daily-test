import os, sys
from importlib import import_module
 
def foo():
    try:
        if not os.path.exists("D:/workspace/test_python/python-daily-test/test"):
            print('file is not existed.')
            return
        sys.path.append("D:/workspace/test_python/python-daily-test/test")
        newModule = import_module('mainForClass-2')
        print(newModule.__name__)
        for it in newModule.__dict__:
            if it.startswith('TY'):
                print('*'*10, it, type(it))
                clsIt = getattr(newModule, it)
                print(clsIt, type(clsIt))
                clsIt()
    except ImportError as e:
        print(" -- load error.", e)

    print(' continue...')

if __name__ == '__main__':
    foo()
