import os, sys, time
import threading

threading.enumerate()

def testFoo1():
    for _ in range(3):
        print(' running ... parents{} current {}\n'.format(os.getppid(), os.getpid()))
        time.sleep(1)

#os.popen(cmd)

if __name__ == '__main__':
    testFoo1()