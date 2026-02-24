import time
import sys
import os
import logging
from watchdog.events import FileSystemEventHandler
# 必须使用 PollingObserver 以支持 SMB [1]
from watchdog.observers.polling import PollingObserver

# 配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class NetworkAwareHandler(FileSystemEventHandler):
    def on_created(self, event):
        logging.info(f"检测到创建: {event.src_path}")

    def on_deleted(self, event):
        # SMB 断开瞬间可能会误报删除，建议在此处增加校验
        if os.path.exists(os.path.dirname(event.src_path)):
             logging.info(f"检测到删除: {event.src_path}")
        else:
             logging.warning(f"忽略可能的误报删除 (路径不可达): {event.src_path}")

def run_monitor_session(path):
    """
    运行单次监控会话。
    如果网络断开或线程死亡，抛出异常跳出，由外层负责重启。
    """
    if not os.path.exists(path):
        raise OSError("目标路径无法访问，等待重试...")

    observer = PollingObserver(timeout=2.0) # 适当增加 timeout 减轻 SMB 负载
    handler = NetworkAwareHandler()
    observer.schedule(handler, path, recursive=True)
    observer.start()
    logging.info(f"监控已启动 (Polling): {path}")

    try:
        # 守护循环
        while True:
            time.sleep(3) # 每3秒检查一次健康状态
            
            # 检查点 1: 检查 Watchdog 线程组是否健康
            if not observer.is_alive():
                raise RuntimeError("Watchdog Observer 线程意外终止")
            
            # 检查点 2: 主动探测 SMB 连通性
            # 这是防止 Emitter 挂了但 Observer 还没死，或者网络断了但还没抛错的关键
            try:
                # 尝试轻量级访问，如列出目录（不必读取文件）
                # 这一步如果因为网络断开报错，会被下方 except 捕获
                os.listdir(path) 
            except OSError:
                raise OSError("SMB 网络连接已断开")

    except Exception as e:
        logging.error(f"监控会话异常: {e}")
        # 遇到任何问题，停止当前 observer
        observer.stop()
        observer.join()
        raise e # 重新抛出，通知外层重启

if __name__ == "__main__":
    # SMB 网络路径
    SMB_PATH = r"\\192.168.1.100\SharedData"
    
    # 也可以是映射盘符，如 Z:\
    # SMB_PATH = r"Z:\"

    logging.info("--- 系统启动，准备接入 SMB ---")

    while True:
        try:
            run_monitor_session(SMB_PATH)
        except KeyboardInterrupt:
            logging.info("用户停止")
            sys.exit(0)
        except Exception as e:
            logging.warning(f"等待恢复... (原因: {e})")
        
        # 发生故障后的冷却时间，避免疯狂重连
        time.sleep(10) 