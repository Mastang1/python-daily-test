# fix 1
#ftpContexts.py

class TftpContextServer(TftpContext):
    def __init__(self,
                 host,
                 port,
                 timeout,
                 root,
                 dyn_file_func=None,
                 upload_open=None,
                 retries=DEF_TIMEOUT_RETRIES,
                 data_port=None):  # 新增data_port参数
        TftpContext.__init__(self,
                             host,
                             port,
                             timeout,
                             retries)
        # ... 其他原有代码 ...
        
        # 修改socket绑定逻辑
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if data_port:  # 如果指定了数据端口
            self.sock.bind(('0.0.0.0', data_port))  # 绑定到指定端口


#fix 2
#TftpServer.py

# 在listen方法中添加data_port参数
def listen(self, listenip="", listenport=DEF_TFTP_PORT,
           timeout=SOCK_TIMEOUT, retries=DEF_TIMEOUT_RETRIES,
           data_port=None):  # 新增参数
    
    # ... 原有代码 ...

    # 修改会话创建部分
    self.sessions[key] = TftpContextServer(raddress,
                                         rport,
                                         timeout,
                                         self.root,
                                         self.dyn_file_func,
                                         self.upload_open,
                                         retries=retries,
                                         data_port=data_port)  # 传递数据端口
    
#called

server = TftpServer()
server.listen(listenport=69, data_port=2000)  # 控制端口69，数据端口2000