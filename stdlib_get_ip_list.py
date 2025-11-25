import socket
import subprocess
import platform

def get_ipv4_simple():
    """简单方法获取IPv4地址（仅使用标准库）"""
    ipv4_addresses = []
    
    try:
        # 方法1: 使用socket
        hostname = socket.gethostname()
        ip_list = socket.gethostbyname_ex(hostname)[2]
        
        for ip in ip_list:
            if ':' not in ip:  # 排除IPv6
                ipv4_addresses.append(ip)
                
    except Exception as e:
        print(f"获取IP地址时出错: {e}")
    
    return ipv4_addresses

def get_ipv4_from_cmd():
    """使用命令行工具获取IP地址（Windows系统）"""
    try:
        if platform.system() == "Windows":
            # 使用ipconfig命令
            result = subprocess.run(['ipconfig'], capture_output=True, text=True)
            lines = result.stdout.split('\n')
            
            ipv4_addresses = []
            for line in lines:
                if 'IPv4' in line:
                    parts = line.split(':')
                    if len(parts) > 1:
                        ip = parts[1].strip()
                        if ip and ip != '127.0.0.1':
                            ipv4_addresses.append(ip)
            
            return ipv4_addresses
    except Exception as e:
        print(f"使用命令行获取IP时出错: {e}")
        return []

def main_simple():
    print("简单IPv4地址获取工具")
    print("-" * 40)
    
    # 获取IP地址
    ips = get_ipv4_simple()
    print(f"简单方法获取的IPv4地址: {ips}")
    if ips:
        print("找到的IPv4地址:")
        for i, ip in enumerate(ips, 1):
            print(f"{i}. {ip}")
    else:
        print("未找到IPv4地址")
    
    """
    # 使用命令行方法
    cmd_ips = get_ipv4_from_cmd()
    if cmd_ips:
        print("\n命令行获取的IPv4地址:")
        for i, ip in enumerate(cmd_ips, 1):
            print(f"{i}. {ip}")
    """
if __name__ == "__main__":
    main_simple()
