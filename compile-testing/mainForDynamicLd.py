import os, sys
from importlib import import_module
projPath = os.path.dirname(os.path.abspath(__file__))
pluginPath = os.path.join(projPath, 'plug_in')
os.makedirs(name=pluginPath, exist_ok=True)

def foo():
    try:
        sys.path.append(pluginPath)
        newModule = import_module('relay')
        print(newModule.__name__)
        for it in newModule.__dict__:
            if it.startswith('typ'):
                print('*'*10, it, type(it))
                targetFun = getattr(newModule, it)
                print(targetFun, type(targetFun))
                targetFun()
    except ImportError as e:
        print(" -- load error.", e)


if __name__ == '__main__':
    foo()
