import inspect
"""Return true if the object is a user-defined function.

Function objects provide these attributes:
    __doc__         documentation string
    __name__        name with which this function was defined
    __code__        code object containing compiled function bytecode
    __defaults__    tuple of any default values for arguments
    __globals__     global namespace in which this function was defined
    __annotations__ dict of parameter annotations
    __kwdefaults__  dict of keyword only parameters with defaults"""

#This is a better implementation
def fooFunc(paramList = [1,2,3,4,5,6], paramVal = None):
    localParam = 'nice day.'
    '''repeat:5'''
    print(' -- ',paramVal)
    def sub():
        arg1 = 100
        print(sub)

if __name__ == '__main__':
    print(fooFunc.__dict__         )
    print(fooFunc.__doc__         )
    print(fooFunc.__name__        )
    print(fooFunc.__code__        )
    print(fooFunc.__defaults__, type(fooFunc.__defaults__[0]))
    print(fooFunc.__globals__     )
    print(fooFunc.__annotations__ )
    print(fooFunc.__kwdefaults__  )
    print(fooFunc.__closure__)
    onCb = fooFunc

    if not onCb.__defaults__ == None:
        #TODO: do some checking
        for itParam in onCb.__defaults__[0]:
            onCb(paramVal=itParam)
    else:
        pass

