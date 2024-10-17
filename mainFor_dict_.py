import sys
import os
import temp
import inspect


def isNotBuiltIn(object):
    if inspect.isbuiltin(object=object):
        return False
    else:
        return True 
    
# for key, value in sys.modules.items():
#     if 'module_' in key and inspect.ismodule(value):
#         print(inspect.getsource(value))
dictModules = {}
# for key, value in sys.modules.items():
#     if 'module_' in key and inspect.ismodule(value):
#         print(key, value)

for key, value in temp.__dict__.items():
    '''This is useful'''
    if 'module_' in key:
        dictModules[key] = value
print(dictModules)