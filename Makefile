.SILENT: fmt check lint

fmt:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		incidentio
	isort --profile black .
	black .

check:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		incidentio
	isort --profile black -c .
	black --check .

lint:
	mypy incidentio
	flake8 .

test:
	pytest -x --cov=core --cov=incidentio --cov-fail-under=90
