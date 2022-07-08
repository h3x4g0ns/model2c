.PHONY: *

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

install: clean
	pip install -e .