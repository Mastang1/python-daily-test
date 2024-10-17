
class AAA:
    dictFoo = {'a':1, 'b':2, 'C':3}

    def __iter__(self):    
        print(self.dictFoo)
        return iter(self.dictFoo.items())
    
if __name__ == '__main__':
    aaa = AAA()
    for it in aaa:
        print(it, type(it), it[0], it[1])