import os,sys

def testFoo():
    def foo():
        val = val2
    strError = None
    try:
        foo()    
    except:
        strError = sys.stderr.read()
        print("error: ", strError)
    
    print(" Today is a nice day.")

class CTest:
    def __init__(self):
        self.list = [1,3,4,5,'hello']
    def index(self):
        print("index")
    def __iter__(self):
        return iter(self.list)
    def run(self):
        for index, value in enumerate(self):
            print(index, value)
if __name__ == '__main__':
    CTest().run()