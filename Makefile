lint:
	blue --check --diff . && isort --check --diff .

doc:
	mkdocs serve

test:
	pytest -s -x --cov=. -vv && coverage html
