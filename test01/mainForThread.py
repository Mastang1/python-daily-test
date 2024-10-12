import threading
import time

# 创建一个条件变量对象
condition_out = threading.Condition()  
# 创建一个容器
items_out = []


# 定义一个生产者线程函数
def producer(condition, items, max_size):
    for i in range(20):
        with condition:  # 进入临界区
            while len(items) >= max_size:
                print(f"达到条件：最大容量{max_size}，当前元素{items}，暂停生产")
                condition.wait()

            print(f"生产元素：{i}")
            items.append(i)
            condition.notify()  # 通知一个等待的消费者线程
            time.sleep(0.2)  # 设置比生产者慢


# 定义一个消费者线程函数
def consumer(condition, items):
    for i in range(20):
        with condition:  # 进入临界区
            while not items:
                condition.wait()  # 等待生产者生产物品

            i = items.pop(0)
            print(f"  - 消费元素：{i}")
            condition.notify()
            time.sleep(0.5)  # 设置比生产者慢


# 创建生产者和消费者线程
producer_thread = threading.Thread(target=producer, args=(condition_out, items_out, 3))
consumer_thread = threading.Thread(target=consumer, args=(condition_out, items_out))

# 启动线程
producer_thread.start()
consumer_thread.start()

# 等待线程完成
producer_thread.join()
consumer_thread.join()

