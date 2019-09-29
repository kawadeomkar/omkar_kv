import basedir
import hashlib
import os
import time
import path
import FileStore

print(os.environ['NAME'], os.getpid())
ADDR = os.environ['STORE']
MASTER = os.environ['MASTER']


def store(env, start_response):
	key = env['REQUEST_URI'].encode('utf-8')
	hashed = hashlib.md5(hashed).hexdigest()

	fs = FileStore(ADDR)
	
	if env['REQUEST_METHOD'] == "GET":
		if fs.file_exists(hashed)
			return [fs.get(hashed)]
		else:
			start_response('404 File not found', [('Content-Type','text/plain')])
			return [b"404 File not found"]	

	elif env['REQUEST_METHOD'] == "PUT":
		fs.put(hashed, env['wsgi.input'].read(int(env.get('CONTENT_LENGTH', 0)))
		
	start_response('200 OK', [('Content-Type','text/html')])
	return [b"Hello World"]
