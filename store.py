import os
import time

print(os.environ['NAME'], os.getpid())

if os.environ['NAME'] == 'store':
	import plyvel
	print(os.environ['DB'])
	db = plyvel.DB(os.environ['DB'], create_if_missing=True)


def store(env, start_response):
	start_response('200 OK', [('Content-Type','text/html')])
	return [b"Hello World"]