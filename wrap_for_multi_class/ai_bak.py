# 方式4: 更高级的动态装饰器，可以指定方法前缀
def apply_method_prefix_decorator(cls, prefix='tcf', external_func=None):
    """
    更通用的函数，用于在运行时为类的特定前缀方法添加装饰器
    
    参数:
        cls: 要装饰的目标类
        prefix: 方法前缀，默认为'tcf'
        external_func: 可选的外部函数，如果为None则使用默认的funEx()
    """
    if external_func is None:
        external_func = funEx
        
    for name, method in vars(cls).items():
        if callable(method) and name.startswith(prefix):
            original_method = method
            
            @wraps(original_method)
            def wrapper(*args, **kwargs, original=original_method):
                external_func()
                return original(*args, **kwargs)
                
            setattr(cls, name, wrapper)
    
    return cls

# 使用方式
apply_method_prefix_decorator(YourClass, 'tcf')  # 为tcf前缀的方法添加装饰器
# 或者
apply_method_prefix_decorator(YourClass, 'if_', my_custom_func)  # 为if_前缀的方法添加装饰器，使用自定义函数
