.SILENT: fmt check lint

download:
	curl \
		"https://converter.swagger.io/api/convert?url=https://api.incident.io/v1/openapi.json" \
		-H "Accept: application/json" \
	| jq -S > incident_io_openapi.json

generate_docs:
	rm -rf docs/api_reference
	poetry run python scripts/api_docs.py \
		-p incident_io_client \
		-d docs/api_reference \
		-m mkdocs.yml

generate_client:
	rm -rf incident_io_client

	poetry run openapi-python-client generate --meta none --path incident_io_openapi.json

	touch incident_io_client/py.typed

fmt:
	pre-commit run --all-files ; exit 0

generate: generate_client generate_docs fmt

lint:
	poetry run mypy incident_io_client scripts
	poetry run flake8 .
