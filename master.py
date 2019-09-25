import os
import time

print(os.environ['NAME'], os.getpid())

if os.environ['NAME'] == 'master':
	import plyvel
	print(os.environ['DB'])
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
		

	
	start_response('200 OK', [('Content-Type','text/plain')])
	return [b"OK"]
