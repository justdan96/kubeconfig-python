SHELL := /bin/bash

.PHONY: tests tidy docs build

tests:
	poetry run pytest -v

tidy: tests
	poetry run pycodestyle kubeconfig tests
	poetry run pyflakes kubeconfig tests
	poetry run pydocstyle kubeconfig
	poetry run pylint kubeconfig

docs:
	pushd docs && make html && popd

build:
	poetry build

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf .cache/
	rm -rf tests/htmlcov/
	rm -rf docs/_build
	rm -rf .pytest_cache
	rm -rf .eggs
