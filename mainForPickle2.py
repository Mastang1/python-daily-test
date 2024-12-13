import pickle
import datetime
from queue import Queue, PriorityQueue

class DataBase:
    def __init__(self, name=None):
        self.listData=[1,3,4,5,6,0]
        self.name = name

class TCF_QUEUE(DataBase):
    def __init__(self, typeOfQ=1, size=1000):
        self.q = PriorityQueue(size)

    def put(self, items=None, block=True, timeout=None):
        self.q.put(item=items, block=block, timeout=timeout)

    def get(self, block=True, timeout=True):
        return self.q.get(block=block, timeout=timeout)
    
class Data:

    def add(self):
        self.listData.append("tangyapeng")


    def display(self):
        print(self.listData)
        print(self.name)

    def __lt__(self, other):
        return self.name < other.name

d1 = Data('tang')
d2 = Data('li')


with open('abc.pk', 'wb') as file_to_write:
    # pickle序列化，然后以二进制的形式存入文件中
    pickle.dump(myQueue, file_to_write)

#inst.assign()

with open('abc.pk', 'rb') as file_to_read:
    # 以二进制的形式进行读取文件
    myInst = pickle.load(file_to_read)
    dataInst = myInst.get()
    print(dataInst, type(dataInst))
    dataInst.display()
