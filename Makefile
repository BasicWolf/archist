help:
	@echo 'Development: '
	@echo '   make test............run unit and integration tests'

buidl: build

build: test

test:
	PYTHONPATH=src/:./ \
	pytest

.PHONY: test