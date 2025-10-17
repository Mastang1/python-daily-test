from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager
import time
import sys

def getTestCases(cls): 
    """ 
    Add testcases 
    Add test environments 
    Dont add fixture testcase and test suite 
    """ 
    FunList = [] 

    inst = cls() 
    # for it in cls.__dict__: 
    for it in dir(inst): 
        if str(it).startswith('_') or str(it).endswith('_'): 
            continue 
        if str(it).startswith("testcase"):  
            method = getattr(inst, str(it), None) 
            FunList.append(method)  
        elif 'setupTestEnv' in str(it) or 'teardownTestEnv' in str(it): 
            method = getattr(inst, str(it), None) 
            FunList.append(method)  
    return FunList, inst

class SharedClass:
    def __init__(self):
        self.mTest = None  # Add member variable

    def testcase_1(self):
        self.mTest = 'testcase_1'
        print("        -- {}".format(self.mTest))

    def testcase_2(self):
        self.mTest = 'testcase_2'
        print("        -- {}".format(self.mTest))

    def testcase_3(self):
        self.mTest = 'testcase_3'
        print("        -- {}".format(self.mTest))

    def testcase_4(self):
        self.mTest = 'testcase_4'
        print("        -- {}".format(self.mTest))

    def testcase_5(self):
        print(" -- {}".format(self.mTest))
class SharedClassManager(BaseManager):
    pass

SharedClassManager.register('SharedClass', SharedClass)

if __name__ == "__main__":
    
    # Create shared class manager
    shared_class_manager = SharedClassManager()
    shared_class_manager.start()

    print(shared_class_manager.SharedClass, type(shared_class_manager.SharedClass), shared_class_manager.SharedClass.__name__)
    print("\n"*10)
    #fix
    classProxy = getattr(shared_class_manager, 'SharedClass')
    retList, inst = getTestCases(classProxy)

    for it in retList:
        print(" -- Case in proxy class: {}".format(it))


    
    # Create and start processes
    processes = []
    for method in retList:
        p = Process(target=method)
        p.start()
        processes.append(p)
        time.sleep(1)
        inst.testcase_5()
    # Wait for all processes to complete
    for p in processes:
        p.join()

