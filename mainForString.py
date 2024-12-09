import os

def strStrip():
    strInput = 'fdfdf\n'
    dataInput = strInput.encode()
    print(dataInput, dataInput[5])
    print(' -- raw data: ', strInput)

    if strInput.endswith('\n'):
        print(f'Target string: {strInput}')

if __name__ == '__main__':
    strStrip()