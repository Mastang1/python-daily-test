import os, sys
from io import StringIO

def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')

def test_unicode():
    # 示例1：将字符串进行编码
    unicode_str = u"Hello, 世界!"
    encoded_str = unicode_str.encode('utf-8')
    print(encoded_str)

    # 输出：b'Hello\xef\xbc\x8c\xe4\xbd\xa0\xe5\xa5\xbd'

    # 示例2：将Unicode字符串进行解码
    decoded_str = encoded_str.decode('utf-8')
    print(decoded_str)

    # 输出：Hello, 世界!

def selfTest():
    '''
    default encoding is : utf-8
    '''
    print(' Current string encode format is : ', sys.stdout.encoding)

    textStr = 'hello, 亚朋'
    byte_str = textStr.encode()#default encode
    utf8Str = byte_str.decode("UTF-8")
    utf16Str = byte_str.decode("gbk")
    print('%s -- %s, and type of them are : %s, %s'%(utf8Str, utf16Str, type(utf8Str), type(utf16Str)))
    # sys.stdout.encoding = 'utf-16'
    # print('%s -- %s, and type of them are : %s, %s'%(utf8Str, utf16Str, type(utf8Str), type(utf16Str)))
    unicode(utf16Str).encode('unicode_escape')
if __name__ == '__main__':
    selfTest()