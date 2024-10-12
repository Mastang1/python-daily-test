import os, sys, pathlib, shutil

# head, tail = os.path.split('/home/user/myfile.txt')
# print("Head:", head) # '/home/user'
# print("Tail:", tail) # 'myfile.txt'

# result = os.path.splitext('/home/user/myfile.txt')
# print(result[1].split('.')[1])
TEST_FOLDER = 'D:\workspace\\test_python\python_test\\file_to_test'
TEST_FOLDER_BAK = 'D:\workspace\\test_python\python_test\\file_to_test-bak'

def testShutil():
    print(os.path.join(TEST_FOLDER, '123.txt'))
    shutil.rmtree(os.path.join(TEST_FOLDER, '123.txt'))
    print(os.listdir(TEST_FOLDER))

def resetFolder():
    try:
        shutil.rmtree(TEST_FOLDER)
    except:
        pass
    finally:
        shutil.copytree(TEST_FOLDER_BAK, TEST_FOLDER)
        print('Done')

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        resetFolder()
        exit()

    match sys.argv[1]:
        case '1':
            testShutil()
