import os

class FileStore:

	def __init__(self, addr):
		self.addr = os.path.realpath(addr)
		os.makedirs(self.addr, exist_ok=True)

	def key_path(key, makedir=False):
		# md5 hash length is 32
		assert len(key) == 32
		path = ADDR + "/" + key[0:1] + "/" + key[0:2]
		# PUT
		if not os.path.isdir(path) and makedir:
			os.makedirs(path, exist_ok=True)
	
		return os.path.join(path, key)
		
		
	def file_exists(self, key):
		return os.path.isfile(self.key_path(key))

	def put(self, key, value):
		try:
			with open(self.key_path(key, True), "wb") as f:
				f.write(value)
				return True
		except:
			return False

	def get(self, key):
		try:
			with open(self.key_path(key), "wb") as f:
				return f.read()
		except:
			return None
			
	def delete(self, key):
		pass

	
