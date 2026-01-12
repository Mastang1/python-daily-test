import importlib
import sys
from pathlib import Path

class ModuleManager:
    def __init__(self):
        self.tool_modules = {}
        self.search_paths = set()

    def add_search_path(self, path):
        """添加模块搜索路径"""
        abs_path = str(Path(path).absolute())
        if abs_path not in self.search_paths:
            sys.path.append(abs_path)
            self.search_paths.add(abs_path)

    def load_tool_module(self, module_name, path=None):
        """动态加载工具模块并缓存到sys.modules"""
        if module_name in self.tool_modules:
            return self.tool_modules[module_name]

        # 添加路径（如果提供）
        if path:
            self.add_search_path(path)

        # 动态导入模块
        module = importlib.import_module(module_name)

        # 双重缓存：管理器内部和sys.modules
        self.tool_modules[module_name] = module
        sys.modules[module_name] = module  # 关键：使其他模块可直接import

        return module

    def get_tool_module(self, module_name):
        """应用模块获取工具模块的接口"""
        return self.tool_modules.get(module_name)

# 单例模式确保全局唯一管理器
module_manager = ModuleManager()
