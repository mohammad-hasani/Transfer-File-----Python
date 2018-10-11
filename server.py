import threading
import os
import socket

def SendFile(sock):
    filename = r'F:\a.jpg'
    sock.send(str(os.path.getsize(filename)) + '\n')
    print str(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        buffer = f.read(1024)
        sock.send(buffer)
        while buffer != '':
            buffer = f.read(1024)
            sock.send(buffer)
        print '[+] Done'

def main():
    s = socket.socket()
    s.bind(('127.0.0.1', 12345))
    s.listen(10)
    print '[+] Listening ...'
    while 1:
        sock, addr = s.accept()
        t = threading.Thread(target=SendFile, args=(sock,))
        t.start()
if __name__ == '__main__':
    main()