# v0.29.0

- updated to the latest API at 2023-07-03

# v0.29.0

- updated to the latest API at 2023-03-27
- added new endpoints:
  - `/v1/incident_roles/{id}`
  - `/v1/incident_types`
  - `/v1/incident_types/{id}`
  - `/v1/openapi.json`
  - `/v1/severities`
  - `/v1/severities/{id}"`
  - `/v2/catalog_entries"`
  - `/v2/catalog_entries/{id}`
  - `/v2/catalog_types`
  - `/v2/catalog_types/{id}/actions/update_schema`

# v0.28.0

- updated to the latest API at 2023-03-20

# v0.28.0

- updated to the latest API at 2023-03-13

# v0.28.0

- updated to the latest API at 2023-03-06

# v0.28.0

- updated to the latest API at 2023-02-20
- added support to new `/v2/incident_updates` endpoint

# v0.27.0

- updated to the latest API at 2023-02-13
- added types for Incident.io Webhooks

# v0.26.0

- updated to the latest API at 2023-01-23
- added `opsgenie_alert` and `datadog_monitor_alert` enum values

# v0.26.0

- updated to the latest API at 2023-01-16

# v0.25.0

- updated to the latest API at 2023-01-09

# v0.24.0

- updated to the latest API at 2022-12-05

# v0.23.0

- updated to the latest API at 2022-10-31

# v0.22.0

- updated to the latest API at 2022-10-24
- new `/v2/incidents` and `/v2/incidents/{id}` endpoints
- new `/v1/incident_roles` and `/v1/incident_roles/{id}` endpoints

# v0.21.0

- updated to the latest API at 2022-10-03
- marked `/v1/incidents` and `/v1/incidents/{id}` as deprecated

# v0.20.0

- updated to the latest API at 2022-09-26
- new `/api/public/v2/incidents` endpoints supported

# v0.19.0

- updated to the latest API at 2022-09-19
- new max length of 1000 charactes for `description` fields

# v0.18.0

- updated to the latest API at 2022-08-29
- removed the `exclude_test_incidents` from `GET /v1/actions`

# v0.17.0

- updated to the latest API at 2022-08-22
- removed tutorial type of incident

# v0.16.0

- updated to the latest API at 2022-08-15
- added `incident_id` in `GET /v1/incident_attachments`

# v0.16.1

- relaxed version of `httpx` to be compatible on som version of Google Cloud Composer

# v0.15.0

- updated to the latest API at 2022-08-08
- added `assignee` field to `ActionsShowResponseBody`, `ActionResponseBody`, `ActionsListResponseBody`
- added new `/v1/incident_attachments` endpoint

# v0.14.0

- updated to the latest API at 2022-08-01
- deprecated `exclude_test_incidents` in `GET /v1/actions` in favour of the `incident_mode` param

# v0.13.0

- updated to the latest API at 2022-07-25
- added `incident_type` to `IncidentResponseBody`

## Breaking chnages

- removed `type` attribute from `IncidentResponeBody`

# v0.12.0

- updated to the latest API at 2022-07-18

# v0.11.0

- updated to the latest API at 2022-07-11

# v0.10.0

- dropped support for Python 3.7
- increase minimum version of `httpx` to avoid [Improper Input Validation in httpx](https://github.com/advisories/GHSA-h8pj-cxx2-jfg2)
- updated to the latest API at 2022-06-20

# v0.9.1

- updated to the latest API at 2022-06-13

# v0.9.0

- updated to the latest API at 2022-06-06

# v0.8.0

- updated to the latest API at 2022-05-28
- added command to donwload the Swagger 2.x specs from the API endpoint

# v0.7.0

- updated to the latest API at 2022-05-26

# v0.6.0

- updated to the latest API at 2022-05-05
- added a new `mode` field in the incidend model, the field's content is the same as the `type` field; the `type` field is now considered deprecated

# v0.5.0

- updated to the latest API at 2022-04-29
- patch to add back `reporter` in the `IncidentRoleResponseBody` schema; this is for incidents created before the latest API update which removed the `reporter` item
