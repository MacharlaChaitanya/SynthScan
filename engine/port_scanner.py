import socket
from concurrent.futures import ThreadPoolExecutor


COMMON_PORTS = [
    21,   # FTP
    22,   # SSH
    23,   # Telnet
    25,   # SMTP
    53,   # DNS
    80,   # HTTP
    110,  # POP3
    143,  # IMAP
    443,  # HTTPS
    3306, # MySQL
    8080  # HTTP-alt
]


def check_port(target, port):
    """
    Checks if a single port is open
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            return port

    except:
        pass

    return None


def scan_ports(target):
    """
    Scans common ports using multithreading
    """

    open_ports = []

    with ThreadPoolExecutor(max_workers=50) as executor:

        results = executor.map(lambda p: check_port(target, p), COMMON_PORTS)

        for port in results:
            if port:
                open_ports.append(port)

    return open_ports