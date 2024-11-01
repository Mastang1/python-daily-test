from multiprocessing import Process,Manager
import multiprocessing
import os, time

def processFunc(listInput):
    print('\n\n\nStart to execute process...')
    if not isinstance(listInput, multiprocessing.managers.ListProxy):
        print('Parameter error.')
        return
    while True:
        time.sleep(1)
        if callable(listInput[0]):
            func = listInput[0]
            print(func, type(func))
            print( '\n' ,'='*80)
            func()

class myClass:
    def __init__(self) -> None:
        self.argv = 'Initialization'

    def foo(self):
        self.argv = str(os.getpid())
        print(' Called the shared function: {}\n\n'.format(self.argv))

if __name__ == '__main__':
    my_class = myClass()
    manager = Manager()
    sharedList = manager.list()          # 生成一个列表,用于在多个进程之间共享
    sharedList.append(my_class.foo)

    print('*'*20)
    func = sharedList[0]
    print(func, type(func))
    func()

    p = Process(target=processFunc,args=(sharedList,))
    p.start()

    pp = Process(target=processFunc,args=(sharedList,))
    pp.start()
    # p.join()
    while True:
        strVal = input()
        if strVal.strip() == 'quit':
            p.terminate()
            pp.terminate()
            break
        p.join()
        pp.join()

