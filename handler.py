
from dataClass import data
from file_system import FindFile
from file_system import SendFile
from file_system import FileNotFound
from time import ctime
def Request_Handler(reqst):
    request = reqst.splitlines()
    print request
    print reqst
    if len(request) == 0:
    	return data([], '', 0)
    req = request[0]
    request.remove(req)
    print request
    header_lines = {}	
    for item in request:
        header = item.split(":")
        if len(header) < 2:
            continue
	key = header[0]
    	value = header[1]
    	header_lines[key] = value
	req = req.split()
	file_dir = req[1]
	
	print header_lines
	print file_dir
	return data(header_lines, file_dir, 1)


def Response_Handler(Data, sock):
	exist = FindFile(Data)
	data.sock = sock
	if exist :
		SendFile(Data)
	else:
		FileNotFound(Data)
		
		
