help:
	@echo 'Development: '
	@echo '   make build...........run all static analyzers and tests'
	@echo '   make buidl...........run essential static analyzers and tests'
	@echo '   make flake8..........run flake8 static code analyzer'
	@echo '   make test............run unit and integration tests'
	@echo '   make mypy............run mypy static type checker'
	@echo '   make pyright.........run pyright static type checker'


buidl: flake8 mypy test

build: flake8 mypy pyright test

flake8:
	flake8 src/ test/

mypy:
	mypy --check-untyped-defs src/ test/

pyright:
	pyright src/ test/

test:
	PYTHONPATH=src/:./ \
	pytest test/

.PHONY: test mypy flake8
