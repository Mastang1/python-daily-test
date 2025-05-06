import pytest

def test_addition():
    """测试加法"""
    print("运行加法测试")
    assert 1 + 1 == 2

def test_subtraction():
    """测试减法"""
    print("运行减法测试")
    assert 5 - 3 == 2

def test_multiplication():
    """测试乘法"""
    print("运行乘法测试")
    assert 2 * 3 == 6

def test_division():
    """测试除法"""
    print("运行除法测试")
    assert 8 / 2 == 4

def test_string_concat():
    """测试字符串拼接"""
    print("运行字符串拼接测试")
    assert "Hello" + " " + "World" == "Hello World"

def test_list_length():
    """测试列表长度"""
    print("运行列表长度测试")
    assert len([1, 2, 3]) == 3

def test_dict_keys():
    """测试字典键"""
    print("运行字典键测试")
    d = {"a": 1, "b": 2}
    assert "a" in d.keys()

def test_boolean():
    """测试布尔值"""
    print("运行布尔值测试")
    assert True is True