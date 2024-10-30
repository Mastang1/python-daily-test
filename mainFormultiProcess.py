"""
Create multiprocess and test multiprocess commucation with each other
key: Pipe()
"""
import os, time
from multiprocessing import Process, Pipe
from threading import Thread

def testcaseMethod():
    print(' This is a testcase.')
    return 'Passed'



class myThread(Thread):
    def __init__(self):
        super().__init__()
        self.subProcess = None

    def run(self):

        global tcsWrapper
        def tcsWrapper():
            testcaseMethod()

        parent_conn, child_conn = Pipe()
        print('  -- Start a child thread.')
        
        p = Process(target=func, args=(child_conn, ))
        self.subProcess = p
        # 生成一个进程，并开始运行新的进程
        p.start()
        parent_conn.send(tcsWrapper)
        p.join(timeout=10)
        # print("## Main process: received:{}".format(parent_conn.recv()))
        if p.is_alive():
            p.terminate()

        print('  -- Thread quit.')
        # p.terminate()
        # p.join()

    def getSubProcess(self):
        return self.subProcess

def func(pipe):
    # 输出传入的参数，当前子进程的进程ID，当前进程的父进程ID
    print(' ## Start a child process')
    while True:
        time.sleep(1)
        # print(os.getpid(), os.getppid())
        pipe.send('I am child process, ID is: {}'.format(pipe.recv()()))


def test():
    # 打印当前进程的进程ID
    print(os.getpid())
    print('main process start...')
    my_thread = myThread()
    my_thread.start()
    my_thread.join()
    time.sleep(5)
    print("\n\n  -- kill child Process")
    my_thread.getSubProcess().terminate()

    print('main process end!')

if __name__ == '__main__':
    test()


    
