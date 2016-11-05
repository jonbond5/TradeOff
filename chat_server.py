import httplib, urllib
import socket
from urllib2 import urlopen

def removeHeaders(data):
    while data[0] != "en-US,en;q=0.8":
        data.pop(0)
    data.pop(0)
    return data[0]

TCP_IP = '52.90.176.100'
TCP_PORT = 8000
BUFFER_SIZE = 2000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:    
    conn, addr = s.accept()

    print 'Connection address:', addr

    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print data
        cleanData = removeHeaders(data.split())
        print type(cleanData)
        conn.send(cleanData)
        conn.close()
        print "Done\n"
        break

