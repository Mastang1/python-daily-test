import importlib
from importlib.util import find_spec
 

def testModule(module_name):

    # 尝试卸载module
    spec = find_spec(module_name)
    if spec is not None:
        importlib.unimport_module(module_name)
        print(f"Module {module_name} has been unloaded.")
    else:
        print(f"Module {module_name} was not imported or does not exist.")

if __name__ == '__main__':
    testModule('temp')