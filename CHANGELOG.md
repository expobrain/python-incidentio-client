# v0.7.0

- updated to the latest API at 2022-05-26

# v0.6.0

- updated to the latest API at 2022-05-05
- added a new `mode` field in the incidend model, the field's content is the same as the `type` field; the `type` field is now considered deprecated

# v0.5.0

- updated to the latest API at 2022-04-29
- patch to add back `reporter` in the `IncidentRoleResponseBody` schema; this is for incidents created before the latest API update which removed the `reporter` item
