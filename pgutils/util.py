
from contextlib import closing 
import socket

def portIsAvailable(port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        try:
            s.bind(("127.0.0.1",port))
        except socket.error as e:
            if e.errno == socket.errno.EADDRINUSE:
                return False
        return True

def seekport():
    p = 0
    available = False
    while not available and p < 9999:
        p += 1
        available = portIsAvailable(p)

    if p == 9999:
        raise ValueError("No free ports")
    return p
