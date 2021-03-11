from xmlrpc.server import SimpleXMLRPCServer
import os

server = SimpleXMLRPCServer(('localhost',9000))

def server_receive_file(self,arg):
	with open("Desktop/cries", "wb") as handle:
		handle.write(arg.data)
		return True

server.register_function(server_receive_file, 'receive file')
server.serve_forever()
