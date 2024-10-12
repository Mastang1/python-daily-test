import signal
import time

def interruptHandler(signum, frame):
    print('You pressed Ctrl+C! Exiting program.')
    exit(0)
 
# 设置中断处理函数
signal.signal(signal.SIGINT, interruptHandler)
 
# 模拟程序运行
try:
    while True:
        print("Program is running. Press Ctrl+C to exit.")
        time.sleep(1)
except KeyboardInterrupt:
    pass  # 这里不需要做任何处理，因为中断处理函数已经被调用