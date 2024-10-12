import os

def test_os_walk():
    all_files = []
    test_root = os.getcwd()
    test_root += '/../tool_report'

    for root, dirs, files in os.walk('D:/workspace/test_python/python_test/tool_report'):
        all_files.append(files)
    print(all_files)



if __name__ == '__main__':
    test_os_walk()