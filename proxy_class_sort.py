from multiprocessing.managers import BaseManager
import inspect

# 原始类定义（方法按 method1 -> method2 -> method3 顺序）
class ClassA:
    def amethod1(self):
        return "method1"
    
    def zmethod2(self):
        return "method2"
    
    def cmethod3(self):
        return "method3"

# 派生 BaseManager 的子类（推荐做法）
class MyManager(BaseManager):
    pass  # 可在此添加自定义方法或属性（如无需扩展可留空）

def test_proxy_class_sort():
    # 注册类到自定义子类 MyManager（而非直接注册到 BaseManager）
    MyManager.register("ClassA", ClassA)
    # 启动自定义管理器并创建代理对象
    manager = MyManager()
    manager.start()
    # 从自定义子类 MyManager 获取代理类（而非 BaseManager）
    myClass = getattr(manager, "ClassA")  # 获取代理类
    proxy_instance = myClass()  # 创建代理对象（真实实例在管理器进程中）

    # ... 以下代码（步骤1-3及验证部分）保持不变 ...
    # 步骤1：从代理对象获取原始类（ClassA）
    # proxy_class = type(proxy_instance)  # 代理类（非原始类）
    # original_class = proxy_class._type  # 原始类（ClassA）
    original_class = ClassA  # 直接引用原始类
    # 步骤2：提取原始类的方法名，按定义顺序排列（Python 3.7+ 保留顺序）
    # 过滤条件：仅保留用户定义的方法（排除特殊方法如 __init__、__class__ 等）


    # method_names = [
    #     name for name, func in inspect.getmembers(original_class, inspect.isfunction)
    #     if not name.startswith("__")  # 排除特殊方法（可选）
    # ]

    #fixed
    method_names = [
        name for name in original_class.__dict__
        if not name.startswith("__")  # 排除特殊方法（可选）
    ]
    for name in method_names:
        print("name:", name) 

    # 步骤3：从代理对象中获取方法，按原始顺序存储
    ordered_methods = [getattr(proxy_instance, name) for name in method_names]

    # 验证结果（打印方法名和调用结果）
    print("方法名（按定义顺序）:", method_names)  # 输出: ['method1', 'method2', 'method3']
    for method in ordered_methods:
        print("调用:", method()) 

    # 关闭管理器
    manager.shutdown()
    
if __name__ == "__main__":
    test_proxy_class_sort()