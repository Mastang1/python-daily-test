import importlib.metadata
from pprint import pprint

def get_dependencies(package_name):
    try:
        requires = importlib.metadata.requires(package_name)
        return requires if requires else []
    except importlib.metadata.PackageNotFoundError:
        return []

# 获取rich库的依赖
deps = get_dependencies('rich')

print("rich库的依赖信息:")
print("=" * 30)
pprint(deps, indent=2, width=80, depth=3)
print("=" * 30)
print(f"共找到 {len(deps)} 个依赖项")