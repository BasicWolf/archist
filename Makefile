help:
	@echo 'Development: '
	@echo '   make build...........run static checks and tests'
	@echo '   make test............run unit and integration tests'
	@echo '   make mypy............run mypy static types checker'


buidl: build

build: mypy pyright test

mypy:
	mypy --check-untyped-defs src test

pyright:
	pyright src/ test/

test:
	PYTHONPATH=src/:./ \
	pytest

.PHONY: test mypy
