import subprocess, time, os

count = 0
while True:
    # 创建子进程
    print("Create subprocess".center(80, '='))
    count+=1
    process = subprocess.Popen(['python', 'tempAsistant.py'])

    # 检查子进程是否完成
    while process.poll() is None:
        print("子进程仍在运行... {}  count{}".format(os.getpid(), count))
        # 可以在这里执行其他操作
        time.sleep(1)
    print("子进程已完成".center(80, '='))



