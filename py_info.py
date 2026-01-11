import sys
import platform

def get_python_info():
    """获取Python环境的详细信息"""
    print("=== Python环境信息 ===")
    print(f"Python版本: {sys.version}")
    print(f"Python版本号: {sys.version_info}")
    print(f"主版本号: {sys.version_info.major}")
    print(f"次版本号: {sys.version_info.minor}")
    print(f"微版本号: {sys.version_info.micro}")
    print(f"发布级别: {sys.version_info.releaselevel}")
    print(f"序列号: {sys.version_info.serial}")
    print(f"平台信息: {platform.platform()}")
    print(f"系统架构: {platform.architecture()}")
    print(f"Python可执行文件路径: {sys.executable}")
    print(f"Python路径: {sys.path}")

if __name__ == "__main__":
    get_python_info()