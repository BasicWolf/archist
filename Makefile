help:
	@echo 'Development: '
	@echo '   make build...........run static checks and tests'
	@echo '   make test............run unit and integration tests'
	@echo '   make mypy............run mypy static types checker'


buidl: build

build: mypy test

mypy:
	mypy --check-untyped-defs src test

test:
	PYTHONPATH=src/:./ \
	pytest

.PHONY: test mypy
