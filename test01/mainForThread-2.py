import threading
import time

# 创建一个条件变量对象
condition_out = threading.Condition()  
# 创建一个容器
items_out = []


# 定义一个生产者线程函数
def producer():
    while True:
        print("... ")
        time.sleep(2)

# 创建生产者和消费者线程
producer_thread = threading.Thread(target=producer)
# 启动线程
producer_thread.start()

time.sleep(3)
# producer_thread.stop()
# 等待线程完成
producer_thread.join()


