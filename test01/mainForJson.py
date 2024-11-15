import json

def jsonCreate():
    data = {'name':'tangyapeng',
            'age':18}
    print(isinstance(data, dict))
    strJson = json.dumps(data)
    print(type(strJson))
    print('data is:', data)
    print('Json string is :', strJson)

def jsonParse():
    print(__name__)
    strIn = '{"name": "tangyapeng", "age": 18}'
    data = json.loads(strIn)
    for subStr in data:
        print(' Element is :', subStr, data[subStr], end= '\n')

def jsonDemo():
    jsonCreate()
    jsonParse()


def testTyp():
    strIn = '{"串口":"COM1", "波特率": 115200, "名字":"通信接口"}'
    data = json.loads(strIn)
    print(data)

if __name__ == '__main__':
    testTyp()