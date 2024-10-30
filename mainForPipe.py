"""
简单示例：使用管道Pipe进行进程间通信
"""
from multiprocessing import Process, Pipe


def func(conn):
    print('send a list object ot other side...')
    # 从管道对象的一端发送数据对象
    conn.send(['33', 44, None])
    conn.close()


if __name__ == '__main__':
    # 默认创建一个双工管道对象，返回的两个对象代表管道的两端，
    # 双工表示两端的对象都可以发送和接收数据，但是需要注意，
    # 需要避免多个进程或线程从一端同时读或写数据
    parent_conn, child_conn = Pipe()
    p = Process(target=func, args=(child_conn, ))
    p.start()
    # 从管道的另一端接收数据对象
    print(parent_conn.recv())
    p.join()
