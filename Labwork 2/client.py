import xmlrpc.client
from pathlib import Path
from xmlrpc.client import Binary

proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

with open("Desktop/cries", "rb") as handle:
	binary_data = xmlrpclib.Binary(handle.read())
	client.server_receiver_file(binary_data)
