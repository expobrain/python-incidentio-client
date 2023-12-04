## v0.36.0 (2023-12-04)

### Fix

- **deps-dev**: bump commitizen from 3.12.0 to 3.13.0 (#341)

## 0.36.0 (2023-12-04)

### Feat

- Updated API at 2023-11-27 (#332)

### Fix

- **deps-dev**: bump mypy from 1.7.0 to 1.7.1 in /example (#333)
- **deps-dev**: bump mkdocs-material from 9.4.10 to 9.4.14 (#334)
- **deps-dev**: bump mkdocstrings-python from 1.7.4 to 1.7.5 (#335)
- **deps-dev**: bump mypy from 1.7.0 to 1.7.1 (#336)
- **deps**: bump httpx from 0.25.1 to 0.25.2 (#337)

## 0.35.3 (2023-11-27)

### Fix

- **deps-dev**: bump types-setuptools from 68.2.0.1 to 68.2.0.2 (#338)

## 0.35.2 (2023-11-20)

### Fix

- **deps-dev**: bump mkdocs-material from 9.4.8 to 9.4.10 (#331)

## 0.35.1 (2023-11-13)

### Fix

- Removed unused tomlim package (#328)

## 0.35.0 (2023-11-13)

### Feat

- Updated API at 2023-11-13 (#319)

### Fix

- reformatted code

## 0.34.2 (2023-11-13)

### Fix

- **deps-dev**: bump black from 23.10.1 to 23.11.0 in /example (#321)
- **deps-dev**: bump mypy from 1.6.1 to 1.7.0 in /example (#322)
- **deps-dev**: bump black from 23.10.1 to 23.11.0 (#323)
- **deps-dev**: bump mkdocstrings-python from 1.7.3 to 1.7.4 (#324)
- **deps-dev**: bump types-setuptools from 68.2.0.0 to 68.2.0.1 (#325)
- **deps-dev**: bump mypy from 1.6.1 to 1.7.0 (#326)

## 0.34.1 (2023-11-13)

### Fix

- **deps-dev**: bump types-pygments from 2.16.0.0 to 2.16.0.1 (#327)

## 0.34.0 (2023-11-06)

### Feat

- Updated API at 2023-11-06 (#317)

### Fix

- formatted code

## 0.33.1 (2023-11-05)

### Fix

- **deps-dev**: Bump mypy from 1.5.1 to 1.6.1 (#316)

## 0.33.0 (2023-11-05)

### Feat

- Updated API at 2023-11-05 (#310)

## 0.32.0 (2023-11-02)

### Feat

- Updated API at 2023-10-23 (#298)

## 0.31.0 (2023-11-02)

### Feat

- Updated API at 2023-10-30 (#305)
- Updated API at 2023-10-16 (#290)

## v0.30.1 (2023-10-01)

## 0.30.1 (2023-10-01)

### Fix

- Added missing package

# v0.30.0

- updated to the latest API at 2023-07-17

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
