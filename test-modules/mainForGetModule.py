import sys
import pkgutil
from importlib import import_module

def dynamicLoader(module_name = None):
    return import_module(module_name)

def delModule(module_name):
    if module_name in sys.modules:
        del sys.modules[module_name]
        print('Delete module: {module_name}.')
    else:
        print('Module: {module_name} is not loaded.')

def testModuleDel(modulename=None):
    sys.modules[modulename].tang.display()
'''
import typ_test_mod

def test():
# 获取当前导入的所有模块
    imported_modules = sys.modules.keys()
    
    # 过滤掉内置模块和当前脚本文件
    non_builtin_modules = [m for m in imported_modules if m not in sys.builtin_module_names and m != '__main__']
    
    # 打印所有非内置模块
    for module in non_builtin_modules:
        if module.startswith('typ_test_mod'):
            print(module, sys.modules[module])
            del sys.modules[module]
            print(typ_test_mod)

def displayTargetModule():
    print('start to test...')
    imported_modules = sys.modules.keys()
    # 过滤掉内置模块和当前脚本文件
    non_builtin_modules = [m for m in imported_modules if m not in sys.builtin_module_names and m != '__main__']
    # 打印所有非内置模块
    for module in non_builtin_modules:
        print(typ_test_mod.tang)
        if module.startswith('typ_test_mod'):
            print(module, sys.modules[module])


# 如果想要递归获取所有包含的子模块，可以使用pkgutil
def iter_modules(module_name=''):
    path = sys.modules[module_name].__path__
    for loader, name, ispkg in pkgutil.iter_modules(path, module_name + '.'):
        if not ispkg:
            print(f"{module_name}.{name}")
 
# 递归打印所有子模块
# for module in sys.modules.values():
#     if '.' not in module.__name__:
#         iter_modules(module.__name__)
'''


'''
We can only delete a module dynamic loaded
'''
if __name__ == '__main__':
    module = dynamicLoader('typ_test_mod')
    print(module, module.__name__)
    delModule(module.__name__)
    del module
    print(module.__name__)