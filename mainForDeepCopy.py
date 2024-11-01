import copy

class myClass:
    """
    This is a test class.
    """

    def __init__(self, argvIn = 'none') -> None:
        self.__argv = str(self)
    
    def func1(self):
        print(self.__argv)

    def func2(self):
        print(self.__argv)

    def set(self, newStr):
        self.__argv = newStr

def test():
    listFunc = []
    my_inst = myClass()
    listFunc.append(my_inst.func1)
    listFunc.append(my_inst.func2)
    print(listFunc)

    # deep copy a list
    print('*'*80, '\n')
    newList = copy.deepcopy(listFunc)
    print(newList)

if __name__ == '__main__':
    test()