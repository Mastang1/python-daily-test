import inspect


def fooFunc():
    param = 0
    param2 = 'hello'
    dictParam = {'1', 1}
    print('Just test')

if __name__ == '__main__':
    val1 = getattr(fooFunc, 'dictParam')
    print(val1, type(val1))
