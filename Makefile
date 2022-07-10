.PHONY: *

clean:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

install: clean
	pip install -e .

build: install
	python -m build

publish: build
	python3 -m twine upload dist/*