from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.severity_response_body import SeverityResponseBody

T = TypeVar("T", bound="SeveritiesShowResponseBody")


@attr.s(auto_attribs=True)
class SeveritiesShowResponseBody:
    """
    Example:
        {'severity': {'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's not really that bad, everyone
            chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        severity (SeverityResponseBody):  Example: {'created_at': '2021-08-17T13:28:57.801578Z', 'description': "It's
            not really that bad, everyone chill", 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1,
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    severity: SeverityResponseBody
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        severity = self.severity.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severity": severity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        severity = SeverityResponseBody.from_dict(d.pop("severity"))

        severities_show_response_body = cls(
            severity=severity,
        )

        severities_show_response_body.additional_properties = d
        return severities_show_response_body

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
