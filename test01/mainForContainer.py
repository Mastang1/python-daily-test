from queue import Queue, PriorityQueue


def prioQTest():
    prioQueue = PriorityQueue(1000)
    prioQueue.put_nowait(item=(1, 2, 3, 4, 5))
    prioQueue.put_nowait(item=(3, 2, 3, 4, 5))
    prioQueue.put_nowait(item=(8, 5, 3, 4, 5))
    prioQueue.put_nowait(item=(8, 2, 3, 4, 5))
    print(prioQueue.queue, prioQueue.qsize())

    while not prioQueue.empty():
        print('*'*80)
        rslt = prioQueue.get()
        print(rslt, type(rslt))

if __name__ == '__main__':
    prioQTest()