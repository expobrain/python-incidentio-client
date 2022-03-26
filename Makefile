.SILENT: fmt check lint

fmt:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		<project-package>
	isort --profile black .
	black .

check:
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		<project-package>
	isort --profile black -c .
	black --check .

lint:
	mypy <project-package>
	flake8 .

test:
	pytest -x --cov=core --cov=<project-package> --cov-fail-under=90
