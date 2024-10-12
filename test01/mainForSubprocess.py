import subprocess

def sub_cmd():
    print(" -- This is a command ")

def process():
    rslt = subprocess.run(["python", "mainForTemp.py"], check=True)
    print(rslt, type(rslt))

if __name__ == '__main__':
    process()