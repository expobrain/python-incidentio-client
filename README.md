# python-incident-io-client

![main build status](https://github.com/expobrain/python-incidentio-client/actions/workflows/main.yml/badge.svg?branch=main)

A client library for accessing incident.io.

## Installation

To install the client:

```shell
pip install python-incidentio-client
```

## Usage

First, create a client:

```python
from incident_io_client import Client

client = Client(base_url="https://api.incident.io")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from incident_io_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.incident.io", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from incident_io_client.models import MyDataModel
from incident_io_client.api.my_tag import get_my_data_model
from incident_io_client.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from incident_io_client.models import MyDataModel
from incident_io_client.api.my_tag import get_my_data_model
from incident_io_client.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.incident.io",
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.incident.io",
    token="SuperSecretToken",
    verify_ssl=False
)
```

Things to know:

1. Every path/method combo becomes a Python module with four functions:

   1. `sync`: Blocking request that returns parsed data (if successful) or `None`
   1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
   1. `asyncio`: Like `sync` but the async instead of blocking
   1. `asyncio_detailed`: Like `sync_detailed` by async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `incident_io_client.api.default`

## Generate code

This client is automatically generated from the Swagger 2.x specs downloaded from the [openapi-python-client](https://pypi.org/project/openapi-python-client/)'s [definition endpoint](https://api-docs.incident.io/#operation/Utilities_OpenAPI); a code generator tool will use the OpenAPI document to generates a sync/async client.

To generare an updated copy of the client:

```shell
poetry install
make download
poetry run make generate
```
