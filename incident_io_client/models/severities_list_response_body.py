from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.severity_response_body import SeverityResponseBody

T = TypeVar("T", bound="SeveritiesListResponseBody")


@attr.s(auto_attribs=True)
class SeveritiesListResponseBody:
    """
    Example:
        {'severities': [{'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's not really that bad, everyone
            chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}, {'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's not really
            that bad, everyone chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        severities (List[SeverityResponseBody]):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            "It's not really that bad, everyone chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
            'updated_at': '2021-08-17T13:28:57.801578Z'}, {'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's
            not really that bad, everyone chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
            'updated_at': '2021-08-17T13:28:57.801578Z'}].
    """

    severities: List[SeverityResponseBody]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        severities = []
        for severities_item_data in self.severities:
            severities_item = severities_item_data.to_dict()

            severities.append(severities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severities": severities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        severities = []
        _severities = d.pop("severities")
        for severities_item_data in _severities:
            severities_item = SeverityResponseBody.from_dict(severities_item_data)

            severities.append(severities_item)

        severities_list_response_body = cls(
            severities=severities,
        )

        severities_list_response_body.additional_properties = d
        return severities_list_response_body

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
