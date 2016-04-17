import os
from time import ctime
def Message_Handler(status, length):
	msg = []
	msg.append("HTTP/1.1 " + str(status) + " OK")
	msg.append("Date " + ctime())
	msg.append("Server: " + "MyHTTPServer")
	msg.append("Content-Length: " + str(length))	
	return msg


def FindFile(Data):
    
	file_dir = os.getcwd() + Data.file_dir
	if os.path.exists(file_dir):
		return True
	else:
		return False
		
	
def SendFile(Data):
	file_dir = os.getcwd() + "/html" + Data.file_dir
	sock = Data.sock
	if os.path.isdir(file_dir) or Data.file_dir == '/':
		file_dir = file_dir  + "main.html"
		files = open(file_dir)
		strs = files.read()
		length = len(strs)
		msg = Message_Handler(200, length)
		for item in msg:
			print item
			sock.send(item)
		#sock.send(strs)
		


def FileNotFound(Data):
	print "File not found"

