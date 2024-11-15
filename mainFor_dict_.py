import sys
import os
import tempMain
import inspect
from importlib import import_module

class BaseOne:
    pass

class TestClass(BaseOne):
    param1 = [1,2,3,4]
    def foo1(self):
        print(self.__class__.__name__)
    def foocls(cls):
        print(cls.__name__)

def isNotBuiltIn(object):
    if inspect.isbuiltin(object=object):
        return False
    else:
        return True 
    
# for key, value in sys.modules.items():
#     if 'module_' in key and inspect.ismodule(value):
#         print(inspect.getsource(value))
def test01(obj):
    dictModules = {}

    for key, value in obj.__dict__.items():
        '''This is useful'''
        if 'module_' in key:
            dictModules[key] = value
    print(dictModules)
def test05(obj):

    for key, value in obj.__dict__.items():
        if 'module' in key:
            print(key, ':   ', value)
def test02():
    # ret = inspect.getmro(TestClass)
    # for it in ret:
    #     print(it.__name__, type(it))

    retMember = inspect.getmembers(tempMain)
    print(type(retMember))
    for it in retMember:
        print(type(it), it)

def testModuleLoad():
    strNameList = [name for name in sys.modules.keys() if 'temp' in name]
    print(strNameList)
    # del sys.modules[strNameList[0]]
    # strNameList = [name for name in sys.modules.keys() if 'temp' in name]
    # print(strNameList)
    handTemp = sys.modules[strNameList[0]]
    '''How to call them ?'''
    for key, value in handTemp.__dict__.items():
        print(key, value)
        if 'module_' in key:
            pass

def testGlobalLocalFun():
    print(globals())
    print('*'*80)
    print(locals())

def testImportPkg():
    curPath = os.path.dirname(os.path.abspath(__file__))
    pkgPath = os.path.join(curPath, 'temp')

    sys.path.append(pkgPath)
    newpkg = import_module(name='temp')
    return newpkg
    

if __name__ == '__main__':
    newPkg = testImportPkg()
    test05(newPkg)