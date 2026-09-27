lint:
	blue --check --diff . && isort --check --diff .

doc:
	mkdocs serve

test:
	make lint && pytest -s -x --cov=. -vv && coverage html
