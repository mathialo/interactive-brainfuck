build:
	bython -c -o python src/*
	yapf -i python/*.py

all: build
