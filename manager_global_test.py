from multiprocessing.managers import BaseManager
from multiprocessing import Process
import os, sys

class classOther:
    staticValue = "classOther static value"

class A:
    
    def __init__(self):
        self.various = classOther.staticValue
        self.value = "A instance"
        print(f"\n\nA instance created in process {os.getpid()}")
        print("A instance various:", self.various, classOther)
        classOther.staticValue = "A static value"


class B:
    

    def __init__(self):
        self.various = classOther.staticValue
        self.value = "B instance"
        print(f"\n\nB instance created in process {os.getpid()}")
        print("B instance various:", self.various, classOther)



class MyManager(BaseManager):
    pass

MyManager.register('A', A)
MyManager.register('B', B)

def workerA(manager):
    a_proxy = manager.A()

def workerB(manager):
    b_proxy = manager.B()


if __name__ == '__main__':
    print(f"Main process: {os.getpid()}")
    
    manager = MyManager()
    manager.start()
    
    a_process = Process(target=workerA, args=(manager,))
    b_process = Process(target=workerB, args=(manager,))

    a_process.start()
    b_process.start()
    
    a_process.join()
    b_process.join()
