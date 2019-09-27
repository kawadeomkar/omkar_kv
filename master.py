import os
import time
import requests
import plyvel

print(os.environ['NAME'], os.getpid())
print(os.environ['DB'])

# instantiate globals
NAME = os.environ['NAME']
DB = os.environ['TYPE']
HOST = os.environ['HOST']

# start plyvel DB
db = plyvel.DB(os.environ['DB'], create_if_missing=True)


def master(env, start_response):
	for k, v in env.items():
		print(k, v)
	

	if env["REQUEST_METHOD"] == "GET":
		key = db.get(env["REQUEST_URI"].encode('utf-8'))
	
		# KEY ERROR
		if key is None:
			response = '404 Key not found'
			start_response(response, [('Content-Type','text/plain')])
			return [bytes(response, 'utf-8')]

	elif env["REQUEST_METHOD"] == "PUT":
		key = db.get(env["REQUEST_URI"].encode('utf-8'))
		
		if key is not None:
			""" KEEP OR DELETE NEW PUT?
			response = '409 Key Exists'		
			start_response(response, [('Content-Type','text/plain')])
			return [bytes(response, 'utf-8')]
			"""
			# override new PUT call
			requests.delete(HOST + "/" + key)

	
	start_response('200 OK', [('Content-Type','text/plain')])
	return [b"OK"]
