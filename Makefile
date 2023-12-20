install-dev:
	@pip install -r requirements-dev.txt

install:
	@pip install -r requirements.txt

build: clean
	@python setup.py sdist bdist_wheel

clean:
	@rm -rf build dist auth.* *.egg-info

check-build:
	@twine check dist/*

test-upload:
	@twine upload --repository testpypi dist/*

upload:
	@twine upload dist/*

pre-commit:
	@pre-commit install

initial-tag:
	@git tag -a -m "Initial tag." v0.0.1

init-cz:
	@cz init

bump-tag:
	@cz bump --check-consistency --changelog

# build|ci|docs|feat|fix|perf|refactor|style|test|chore|revert|bump

lint:
	@black google_calendar/
	@isort google_calendar/
	@flake8 google_calendar/

install-calendar:
	pip uninstall /home/lyle/libraries/google-calendar/dist/google_calendar-0.0.1-py3-none-any.whl
	pip install /home/lyle/libraries/google-calendar/dist/google_calendar-0.0.1-py3-none-any.whl
