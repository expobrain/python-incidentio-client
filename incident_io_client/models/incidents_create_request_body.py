from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.custom_field_entry_payload_request_body import (
    CustomFieldEntryPayloadRequestBody,
)
from ..models.incidents_create_request_body_visibility import (
    IncidentsCreateRequestBodyVisibility,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentsCreateRequestBody")


@attr.s(auto_attribs=True)
class IncidentsCreateRequestBody:
    """
    Example:
        {'custom_field_entries': [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it'},
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it'},
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it'}]},
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it'}]}], 'idempotency_key': 'alert-uuid', 'name': 'Our
            database is sad', 'severity_id': 'Optio qui ea accusamus iure.', 'summary': "Our database is really really sad,
            and we don't know why yet.", 'visibility': 'public'}

    Attributes:
        custom_field_entries (List[CustomFieldEntryPayloadRequestBody]): Set the incident's custom fields to these
            values Example: [{'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it'},
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it'},
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it'}]},
            {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it'}, {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link':
            'https://google.com/', 'value_numeric': '123.456', 'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'value_text': 'This is my text field, I hope you like it'}]}, {'custom_field_id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'values': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it'},
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it'},
            {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_link': 'https://google.com/', 'value_numeric': '123.456',
            'value_option_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'value_text': 'This is my text field, I hope you like it'}]}].
        idempotency_key (str): Unique string used to de-duplicate incident create requests Example: alert-uuid.
        severity_id (str):  Example: Et aliquid..
        visibility (IncidentsCreateRequestBodyVisibility): Whether the incident is public or private Example: public.
        name (Union[Unset, str]): Explanation of the incident Example: Our database is sad.
        summary (Union[Unset, str]): Detailed description of the incident Example: Our database is really really sad,
            and we don't know why yet..
    """

    custom_field_entries: List[CustomFieldEntryPayloadRequestBody]
    idempotency_key: str
    severity_id: str
    visibility: IncidentsCreateRequestBodyVisibility
    name: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        custom_field_entries = []
        for custom_field_entries_item_data in self.custom_field_entries:
            custom_field_entries_item = custom_field_entries_item_data.to_dict()

            custom_field_entries.append(custom_field_entries_item)

        idempotency_key = self.idempotency_key
        severity_id = self.severity_id
        visibility = self.visibility.value

        name = self.name
        summary = self.summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_entries": custom_field_entries,
                "idempotency_key": idempotency_key,
                "severity_id": severity_id,
                "visibility": visibility,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        custom_field_entries = []
        _custom_field_entries = d.pop("custom_field_entries")
        for custom_field_entries_item_data in _custom_field_entries:
            custom_field_entries_item = CustomFieldEntryPayloadRequestBody.from_dict(
                custom_field_entries_item_data
            )

            custom_field_entries.append(custom_field_entries_item)

        idempotency_key = d.pop("idempotency_key")

        severity_id = d.pop("severity_id")

        visibility = IncidentsCreateRequestBodyVisibility(d.pop("visibility"))

        name = d.pop("name", UNSET)

        summary = d.pop("summary", UNSET)

        incidents_create_request_body = cls(
            custom_field_entries=custom_field_entries,
            idempotency_key=idempotency_key,
            severity_id=severity_id,
            visibility=visibility,
            name=name,
            summary=summary,
        )

        incidents_create_request_body.additional_properties = d
        return incidents_create_request_body

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
