.PHONY: *

install:
	python3 setup.py install

build:
	python3 setup.py sdist bdist_wheel