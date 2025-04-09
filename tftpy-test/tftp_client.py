import os
import tftpy

def start_fttp_client():
    """
    Starts a TFTP client to download a file from a specified server.

    The function creates a TFTP client instance and attempts to download a file
    named 'test.bin' from the server at '127.0.0.1'. The downloaded data is
    written to a local file named 'rcv.bin'.

    Args:
        None

    Returns:
        None

    Raises:
        tftpy.TftpException: If an error occurs during the TFTP transfer.
    """
    # Create a TFTP client instance
    client = tftpy.TftpClient(host='192.168.4.200', localip='192.168.4.201')

    # Open a local file in binary write mode to store the downloaded data
    with open('rcv.bin', 'wb') as stream_rcv:
        # Download the file 'test.bin' from the server and write it to the local file
        client.download(filename='test.bin', output=stream_rcv)

if __name__ == '__main__':
    # Call the start_fttp_client function to initiate the TFTP download
    start_fttp_client()