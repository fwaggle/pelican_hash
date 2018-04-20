from pelican import signals
import hashlib

def sha256(input):
	return hashlib.sha256(input).hexdigest()

def add_filter(pelican):
	pelican.env.filters.update({'sha256': sha256})

def register():
    signals.generator_init.connect(add_filter)