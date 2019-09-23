import os


def master(env, start_response):
	start_response('200 OK', [('Content-Type','text/html')])
	return [b"Hello World"]
