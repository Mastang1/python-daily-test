'''
class ParamsOneCase:

    def __init__(self, testcaseName = "Mytestcase"):
        self.testCaseName = testcaseName
        self.testMethodNum = 0
        self.methodGrp = []

    def addTestMethod(self, dictMethod = {}):
        self.methodGrp.append(dictMethod)
        self.testMethodNum = self.testMethodNum + 1

    def __call__(self, *args, **kwds):
        return self.at(*args, **kwds)
    
    def at(self, index):
        if index > self.testMethodNum - 1:
            return None
        return self.methodGrp[index]

if __name__ == '__main__':
    ParamsOneCase()

'''
class ParamsOneCase:
    '''
    The class includes all parameters of a sheet.
    '''
    def __init__(self, testcaseName = "Mytestcase"):
        self.testCaseName = testcaseName
        self.testMethodNum = 0
        self.methodGrp = [1,2,3,4,5,6]

    def addTestMethod(self, dictMethod = {}):
        self.methodGrp.append(dictMethod)
        self.testMethodNum = self.testMethodNum + 1

    def __call__(self, *args, **kwds):
        return self.at(*args, **kwds)
    
    def at(self, index):
        return self.methodGrp[index]

if __name__ == '__main__':
    param = ParamsOneCase()
    print(param(1))