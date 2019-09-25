import os
import time

print(os.environ['NAME'], os.getpid())

if os.environ['NAME'] == 'master':
	import plyvel
	print(os.environ['DB'])
	db = plyvel.DB(os.environ['DB'], create_if_missing=True)


def master(env, start_response):
	key = db.get(env["REQUEST_URI"].encode('utf-8'))
	
	if key is None:
	
	
	start_response('200 OK', [('Content-Type','text/html')])
	return [b"OK"]
