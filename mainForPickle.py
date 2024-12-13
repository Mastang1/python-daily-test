import pickle
import datetime



class MyClass:
    myList=[1,2, '3']

    def assign(self):
        self.myList.append('tangyapeng')

    def display(self):
        print(self.myList)

inst = MyClass()
pFoo = inst.display
print(pFoo)


with open('abc.pk', 'wb') as file_to_write:
    # pickle序列化，然后以二进制的形式存入文件中
    pickle.dump(pFoo, file_to_write)

#inst.assign()

with open('abc.pk', 'rb') as file_to_read:
    # 以二进制的形式进行读取文件
    myInst = pickle.load(file_to_read)
    print(myInst)
    print(type(myInst))
    myInst()
