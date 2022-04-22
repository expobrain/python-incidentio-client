.SILENT: fmt check lint

download:
	curl \
  		https://api.incident.io/v1/openapi.json \
		| jq -S . > incident_io_openapi.json

generate:
	rm -rf incident_io_client

	# Version 0.10.8 generates the client in the wrong directory, thsi is fixed in 0.11
	rm -rf incidentio_client

	openapi-python-client generate --meta none --path incident_io_openapi.json

	mv incidentio_client incident_io_client

	touch incident_io_client/py.typed
	make fmt

fmt:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade --exit-zero-even-if-changed --py36-plus {} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		.
	isort --profile black .
	black .

check:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade --py36-plus {} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		.
	isort --profile black -c .
	black --check .

lint:
	mypy .
	flake8 .
