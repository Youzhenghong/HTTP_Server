#coding = UTF-8
from socket import *
from config import *

def ServerInit():
    ServerSocket = socket(AF_INET, SOCK_STREAM)
    ServerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    target = (HOST_IP, HOST_PORT)
    ServerSocket.bind(target)
    ServerSocket.listen(10)
    print "Server is running"
    return ServerSocket
    

def Tcplink(sock, addr):
    print "New Connection from %s " % str(addr)
    request = sock.recv(1024)
    Data = Handle_Request(request)
    response(Data, sock)
    sock.close()
    

def Run_Server():
    ServerSocket = ServerInit()
    print "Waiting for connection"
    while True:
       sock, addr = ServerSocket.accept()
       Tcplink(sock, addr)


