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

tupleParam = (1,'2',[22,33],'nice day')
dictParam = {'arg1':1, 'arg2':2}

def foo(*args, **kw):
    print(args)
    print(kw)

if __name__ == '__main__':
    foo(*tupleParam)
    foo(**dictParam)

