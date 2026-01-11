import subprocess
import paramiko
import threading

# 网段信息
network = "192.168.199"
ping_timeout = 1  # ping超时时间 (秒)
ssh_port = 22     # 默认的SSH端口
ssh_timeout = 3   # SSH连接超时时间 (秒)

# 检测是否可以ping通
def ping_host(ip):
    try:
        # 使用ping命令进行探测，-c 1 表示发送1个包，-w 1 表示超时时间为1秒
        response = subprocess.run(['ping', '-c', '1', '-w', str(ping_timeout), ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
        return False

# 尝试通过SSH连接
def check_ssh(ip):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动添加主机密钥
        client.connect(ip, port=ssh_port, username="root", password="your_password", timeout=ssh_timeout)
        client.close()
        return True
    except paramiko.ssh_exception.AuthenticationException:
        print(f"{ip}: SSH authentication failed")
        return False
    except (paramiko.ssh_exception.NoValidConnectionsError, Exception) as e:
        print(f"{ip}: SSH connection failed - {e}")
        return False

# 检查指定IP的Ping和SSH服务
def check_host(ip):
    print(f"Checking {ip}...")
    if ping_host(ip):
        print(f"{ip} is alive via Ping.")
        if check_ssh(ip):
            print(f"{ip} is accessible via SSH.")
        else:
            print(f"{ip} is not accessible via SSH.")
    else:
        print(f"{ip} is not alive via Ping.")

# 多线程遍历网段中的主机
def scan_network():
    threads = []
    for i in range(1, 255):
        ip = f"{network}.{i}"
        thread = threading.Thread(target=check_host, args=(ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    scan_network()
