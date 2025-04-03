import inspect
"""
{
    'variant_yyyyy': {
        'name': 'variant_yyyyy',
        'type': 'method',
        'doc': 'variant变量注释',
        'params': {
            'param1': {'type': 'str', 'default': None},
            'param2': {'type': 'int', 'default': None}
        }
    },
    'variant_dddd': {
        'name': 'variant_dddd',
        'type': 'method',
        'doc': 'variant变量注释',
        'params': {
            'param1': {'type': 'dict', 'default': None},
            'param2': {'type': 'list', 'default': None},
            'param3': {'type': 'super', 'default': None},
            'param4': {'type': 'float', 'default': None}
        }
    }
}
"""
def get_class_members(cls):
    members = {}
    
    for name, member in inspect.getmembers(cls):
        if not name.startswith('variant_'):
            continue
            
        doc = inspect.getdoc(member)
        member_info = {
            'name': name,
            'type': None,
            'doc': doc,
            'params': {}  # 新增参数信息字段
        }
        
        if inspect.isfunction(member) or inspect.ismethod(member):
            member_info['type'] = 'method'
            # 获取参数信息
            sig = inspect.signature(member)
            for param_name, param in sig.parameters.items():
                member_info['params'][param_name] = {
                    'type': str(param.annotation) if param.annotation != inspect.Parameter.empty else 'Any',
                    'default': param.default if param.default != inspect.Parameter.empty else None
                }
        elif isinstance(member, property):
            member_info['type'] = 'property'
        else:
            member_info['type'] = 'variable'
        
        members[name] = member_info
    
    return members

# 使用示例
class MyClass:
    """类注释"""
    
    """variant变量注释"""
    def variant_yyyyy(self, param1: str, param2:int):
        pass
    
    """variant变量注释"""
    def variant_dddd(self, param1:dict, param2:list, param3:super,  param4:float):
        pass

# 获取类成员信息
print(get_class_members(MyClass))