
class BaseDemo:
    def foo(self):
        print(type(self))
        
    def test(self):
        print(type(self))

class Sub(BaseDemo):    
    def foo(self):
        print(type(self))
    



sub = Sub()
sub.foo()
sub.test()