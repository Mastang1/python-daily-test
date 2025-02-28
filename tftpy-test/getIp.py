import socket

def get_ip_list():
    """
    Get a list of IPv4 addresses associated with the host.

    This function uses the socket module to get a list of all IP addresses
    associated with the host. It filters out the IPv6 addresses and returns
    a list of strings, each representing an IPv4 address.

    Returns:
        list: A list of IPv4 addresses.
    """
    ip_list = []
    hostname = socket.gethostname()
    addresses = socket.getaddrinfo(hostname, None)
    for address in addresses:
        if address[0] == socket.AF_INET:  # Filter for IPv4 addresses
            ip_list.append(address[4][0])
    return ip_list

# Example usage
ip_list = get_ip_list()
print("IPv4 addresses:", ip_list)
