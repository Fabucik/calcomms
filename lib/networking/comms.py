import socket

# socket init if server
def serverInit():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 42865))
    
    return sock

def socketSend(conn, data):
    conn.send(str.encode(data))
    
def socketRecv(conn):
    data = conn.recvfrom(80)[0].decode("utf-8")
    
    return data.strip()