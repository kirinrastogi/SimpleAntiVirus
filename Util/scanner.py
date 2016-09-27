

def md5(fname):
	return hashlib.md5(open(full_path, 'rb').read()).hexdigest()

def scan(fname):
	hash = md5(fname)
	
