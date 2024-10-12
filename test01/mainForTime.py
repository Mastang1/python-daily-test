import os, time
from datetime import datetime
 
'''
test the time of a time of day, and the result is that the instance of time class
can compare with each other.
'''
def test_date_time():
    print(datetime.now().hour)
    timeForStr = datetime.strptime("18:30:01", "%H:%M:%S")
    print(timeForStr, type(timeForStr), timeForStr.time(), type(timeForStr.time()))
    if datetime.now().time() > timeForStr.time():
        print(datetime.now().time())
    else:
        print(timeForStr.time())
if __name__ == '__main__':
    test_date_time()

            