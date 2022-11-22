lint:
	@poetry run flake8 --config flake8.cfg

test:
	@poetry run pytest

coverage:
	@poetry run pytest --cov=custom_mv --cov-report=term --cov-report=xml