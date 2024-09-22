import string,os, sys


# import sys
# savedStdout = sys.stdout  #保存标准输出流
# with open('out.txt', 'w+') as file:
#     sys.stdout = file  #标准输出重定向至文件
#     print('This message is for file!')

# sys.stdout = savedStdout  #恢复标准输出流
# print('This message is for screen!')
# exit()


def testFoo():
    strFoo = str(testFoo)
    # print(strFoo.split(' ')[1], type(strFoo))

def testStdOut():
    with open("tangyapeng.txt", 'w+') as fStream:
        print("start to test: ")
        stderrO = sys.stderr
        stdOutO = sys.stdout

        sys.stderr = fStream
        sys.stdout = sys.stderr 

        print("Hello")
        sys.stderr.write("error")
        try:
            raise ValueError('value error.')
        except Exception as e:
            sys.stderr.write(str(e))
        finally:
            sys.stderr = stderrO 
            sys.stdout = stdOutO 
            print("Done")

   
if __name__ == '__main__':
    testStdOut()


# try:
#     # 这里放置可能引发异常的代码
#     1 / 0  # 示例：一个会引发ZeroDivisionError的除以零的操作
# except Exception as e:  # 捕获所有异常
#     with open('error.log', 'w') as f:  # 打开（或创建）文件用于写入
#         f.write(str(e))  # 写入异常信息
#     raise  # 重新抛出异常，如果需要的话