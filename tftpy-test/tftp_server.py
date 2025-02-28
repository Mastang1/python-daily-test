import multiprocessing
from tftpy import TftpServer
import time
import sys

def start_tftp_server():
    """
    Starts a TFTP server.

    This function initializes a TFTP server using the tftpy library.
    The server is configured to serve files from the current directory.
    It listens on the loopback address (127.0.0.1), which means it will only accept connections from the local machine.

    Returns:
        None
    """
    # Create a TFTP server instance with the current directory as the root directory
    server = TftpServer(tftproot='./')
    # Start the server and listen on the loopback address (127.0.0.1)
    server.listen(listenip='127.0.0.1')

def main():
    """
    Main function to start the TFTP server.

    This function creates a process and starts the TFTP server.
    It allows the server to run in a separate process, enabling concurrent execution.

    Returns:
        None
    """
    # Create a process and start the TFTP server
    tftp_process = multiprocessing.Process(target=start_tftp_server)
    tftp_process.daemon = True
    tftp_process.start()
    # The main process can continue to do other things
    print("TFTP server started in a separate process.")
    time.sleep(10)
    print("TFTP server quit.")
    sys.exit(0)
    

if __name__ == '__main__':
    main()