import pytest
from datetime import datetime

# 模块级fixture
def setup_module(module):
    print("\n=== Module setup ===")

def teardown_module(module):
    print("\n=== Module teardown ===")

# 会话级fixture
@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print("\n*** Session fixture setup ***")
    yield
    print("\n*** Session fixture teardown ***")

# 类级别fixture
@pytest.fixture(scope="class")
def class_fixture():
    print("\n--- Class fixture setup ---")
    yield
    print("\n--- Class fixture teardown ---")

# 函数级fixture带参数
@pytest.fixture
def data_fixture(request):
    print(f"\nFixture setup with param: {request.param}")
    yield request.param * 2
    print("\nFixture teardown")

# 自动使用的fixture
@pytest.fixture(autouse=True)
def auto_fixture():
    print("\nAuto-used fixture setup")
    yield
    print("\nAuto-used fixture teardown")

# 参数化测试
@pytest.mark.parametrize("data_fixture", [1, 2], indirect=True)
def test_parametrized(data_fixture):
    assert data_fixture in [2, 4]

# 测试类使用类级别fixture
@pytest.mark.usefixtures("class_fixture")
class TestDemo:
    # 方法级fixture
    @pytest.fixture
    def method_fixture(self):
        print("\nMethod fixture setup")
        yield datetime.now()
        print("\nMethod fixture teardown")

    def test_method1(self, method_fixture):
        assert isinstance(method_fixture, datetime)

    def test_method2(self, tmp_path):
        temp_file = tmp_path / "test.txt"
        temp_file.write_text("pytest")
        assert temp_file.read_text() == "pytest"
