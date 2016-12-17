test:
	pytest -v

mypy:
	mypy --silent-imports breaking_changes/*.py
