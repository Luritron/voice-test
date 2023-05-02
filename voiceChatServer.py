import socket
import threading

port = 5000
host = "0.0.0.0"

server = socket.socket()
server.bind((host, port))
server.listen(5)

client = []

def start():
    while (True):
        conn, addr = server.accept()
        client.append(conn)
        thr = threading.Thread(target = send, args = (conn, ))
        thr.start()

def send(fromConn):
    try:
        while (True):
            data = fromConn.recv(4096)
            for cl in client:
                if cl != fromConn:
                    cl.send(data)
    except:
        print('Client disconnected')

start()