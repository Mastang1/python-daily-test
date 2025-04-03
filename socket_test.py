import socket
import sys

def check_port(host='127.0.0.1', port=22):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)  # 设置超时时间
            s.connect((host, port))
        return True
    except socket.timeout:
        print("连接超时")
        return False
    except ConnectionRefusedError:
        print("连接被拒绝")
        return False
    except Exception as e:
        print(f"连接失败: {e}")
        return False

if __name__ == "__main__":
    # 获取命令行参数，如果没有指定则使用默认值
    host = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 22
    
    if check_port(host=host, port=port):
        print(f"主机 {host} 的端口 {port} 可用")
    else:
        print(f"主机 {host} 的端口 {port} 不可用")