from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os,sys

WATCH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"{event.src_path} was modified")
 
    def on_created(self, event):
        print(f"{event.src_path} was created")


# 创建事件处理器
event_handler = MyHandler()
 
# 创建监控器，监视当前目录
observer = Observer()
observer.schedule(event_handler, path=WATCH_PATH, recursive=True)
 
# 开始监控
observer.start()
 
try:
    print(WATCH_PATH)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()