import serial
import socket
import os

def enumerate_serial_ports():
    return [f"/dev/{p}" for p in os.listdir("/dev") if "tty" in p]

def test_tcp_connection(host="127.0.0.1", port=80, timeout=1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False
