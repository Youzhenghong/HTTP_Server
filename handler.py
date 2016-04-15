
from dataClass import data


def Handle_Request(reqst):
	request = reqst.splitlines()
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
	return data(header_lines, file_dir)


def response(Data, sock):
	pass
