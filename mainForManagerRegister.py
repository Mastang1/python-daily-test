from multiprocessing import Process,Manager, managers
import multiprocessing
import os, time

def processFunc(method):
    # print('\n -- Start to execute process...{}'.format(os.getpid()))

    method()
    print('Try doing...')
    print('\n\n\n\n')

class myClass:
    def __init__(self) -> None:
        self.argv = 'Initialization'

    def foo(self):
        self.argv = 'Changed'

    def display(self):
        print(self.argv)

class myClass2:
    def __init__(self) -> None:
        self.argv = 'Initialization'

    def foo2(self):
        self.argv = 'Changed'

    def display2(self):
        print(self.argv)

class MyManager(managers.SyncManager):
    pass

class CollectTcs:
    def __init__(self):
        MyManager.register('myClass', myClass)
        MyManager.register('myClass222', myClass2)
        manager = MyManager()
        manager.start()
        self.my_class = manager.myClass()
        self.my_class333 = manager.myClass222()
        self.sharedList = manager.list()
        self.sharedList.append(self.my_class)
        self.sharedList.append(self.my_class333)

if __name__ == '__main__':
    """Create a manager in loader, and collect all data in a shared list or dictionary"""
    # collect_tcs = CollectTcs()
    # my_class = collect_tcs.my_class
    # my_class3 = collect_tcs.my_class333
    # myTcsList = collect_tcs.sharedList
    class R:
        @staticmethod
        def RRR():
            print("rrrrrrr")
    print(locals())

    MyManager.register('R', R)
    mgr = MyManager()
    mgr.start()


    p = Process(target=processFunc,args=(mgr.R.RRR,))
    p.start()




    while True:
        strVal = input()
        if strVal.strip() == 'quit':
            # my_class.display()
            # my_class3.display2()
            p.terminate()
            break
        p.join()

