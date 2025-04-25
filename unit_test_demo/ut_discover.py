import unittest

if __name__ == '__main__':
    # 使用discover自动发现并运行所有测试
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    print("\n\n\n")
    print(test_suite, type(test_suite))
    print("\n\n\n")
    # 运行测试套件
    test_runner = unittest.TextTestRunner(verbosity=0)
    test_runner.run(test_suite)
