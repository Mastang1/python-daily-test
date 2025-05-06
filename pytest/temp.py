import pytest
from _pytest.config import Config
from _pytest.main import Session
from _pytest.nodes import Item
from typing import List
from pytest import Session

def discover_tests(path: str = ".") -> List[str]:
    """发现指定路径下的所有测试用例"""
    # 创建配置对象（使用pytest的hook机制正确初始化）
    config = pytest.Config.fromdictargs({}, [path])
    
    # 创建测试会话
    session = Session.from_config(config)
    
    # 执行测试收集
    session.perform_collect()
    
    # 获取所有测试用例的 nodeid（唯一标识）
    return [item.nodeid for item in session.items]

def run_tests(test_ids: List[str]) -> int:
    """运行指定的测试用例"""
    # 创建配置对象（启用详细输出）
    config = Config()
    config.option.verbose = 1
    config.args = test_ids
    
    # 创建并运行测试会话
    session = Session.from_config(config)
    return session.exitstatus

if __name__ == "__main__":
    # 1. 发现测试用例
    print("发现测试用例...")
    test_cases = discover_tests()
    print(f"找到 {len(test_cases)} 个测试用例:")
    for case in test_cases:
        print(f" - {case}")

    # 2. 运行所有测试
    print("\n运行测试...")
    exit_code = run_tests(test_cases)
    print(f"\n测试完成，退出码: {exit_code}")