build:
	mkdir -p python/ibf python/etc
	bython -c -o python/ibf src/*.by
	yapf -i -r python
	mv python/ibf/bf.py python/etc/ibf
	chmod +x python/etc/ibf
	echo "from . import tokenizer, inputoutput, interpreter" > python/ibf/__init__.py
	cp README.md python/

all: build

install: build
	cd python/ && sudo -H pip3 install .
