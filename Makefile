lint:
	poetry run blue --check --diff . && poetry run isort --check --diff .

doc:
	poetry run mkdocs serve

test:
	poetry run make lint && pytest -s -x --cov=. -vv && poetry run coverage html
