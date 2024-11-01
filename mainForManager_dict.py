from multiprocessing import Process,Manager
import multiprocessing
import os, time,copy

def processFunc(dictCls):
    print('\n\n\nStart to execute process...')
    foo = None
    for func in dictCls[myClass.__name__]:
        if 'GetSelf' in func.__name__:
            foo = func
    
    for _ in range(20):
        time.sleep(1)
        print(foo)


class myClass:
    def __init__(self) -> None:
        self.argv = 'Initialization'

    def foo(self):
        self.argv = str(os.getpid())
        print(' Called the shared function1: {}\n\n'.format(self.argv))

    def foo2(self):
        self.argv = str(os.getpid())
        print(' Called the shared function2: {}\n\n'.format(self.argv))

    def foo3(self):
        self.argv = str(os.getpid())
        print(' Called the shared function3: {}\n\n'.format(self.argv))

    def fooGetSelf(self):
        return self

def getMethodInClass(cls):
    funcList = []
    dictCls = {}
    inst = cls()

    for it in cls.__dict__:
        if it.startswith('foo'):
            method = getattr(inst, it, None)
            funcList.append(method)
    dictCls[cls.__name__] = funcList
    return dictCls

if __name__ == '__main__':
    
    manager = Manager()
    shareDict = manager.dict()

    tempDict = getMethodInClass(myClass)
    shareDict.update(tempDict)
    # shareDict = copy.deepcopy(tempDict)
    # shareDict = tempDict.copy()
    p = Process(target=processFunc,args=(shareDict,))
    p.start()

    while True:
        strInput = input()
        if not strInput is None:
            p.terminate()
            p.join()
            break

