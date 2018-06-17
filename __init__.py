from pelican import signals
import hashlib

def sha256(input):
	return hashlib.sha256(input.encode('utf-8')).hexdigest()

def md5(input):
	return hashlib.md5(input.encode('utf-8')).hexdigest()

def add_filter(pelican):
	pelican.env.filters.update({'sha256': sha256, 'md5': md5})

def register():
    signals.generator_init.connect(add_filter)