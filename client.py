import socket
import os
import threading

def sendFile(sock):
    sock.send(r'F:\a.jpg')
    filezise = sock.recv(1024)
    with open('g.jpg', 'wb') as f:
        mybuffer = sock.recv(1024)
        mybufferlen = len(mybuffer)
        f.write(mybuffer)
        while mybufferlen < filezise:
            mybuffer = sock.recv(1024)
            mybufferlen += 1024
            f.write(mybuffer)
    print '[+] Ok'


def main():
    s = socket.socket()
    s.connect(('127.0.0.1', 12345))
    t = threading.Thread(target=sendFile, args=(s,))
    t.start()

if __name__ == '__main__':
    main()