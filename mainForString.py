import os

def strStrip():
    strInput = input()
    print(' -- raw data: ', strInput)
    print(' -- new data: ', strInput.strip())
if __name__ == '__main__':
    strStrip()