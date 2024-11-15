
import time

def typ_test():
    listTest = []
    for it in range(1000):
        listTest.append(it)

    strInput = input(' please input:')
    if 'ok' in strInput:
        print('\n\n\n'+ "today is a nice day".center(100, '='))
    floatTime = time.time()
    intTime = int(floatTime)
    print(floatTime, intTime)

    for it in listTest:
        print(it)
        time.sleep(0.01)
    time.sleep(3)
if __name__ == '__main__':
    typ_test()