from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.severity_v1 import SeverityV1


T = TypeVar("T", bound="SeveritiesV1ListResponseBody")


@_attrs_define
class SeveritiesV1ListResponseBody:
    """
    Example:
        {'severities': [{'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues with **low impact**.',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at': '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        severities (List['SeverityV1']):  Example: [{'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Issues
            with **low impact**.', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Minor', 'rank': 1, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}].
    """

    severities: List["SeverityV1"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        from ..models.severity_v1 import SeverityV1

        d = src_dict.copy()
        severities = []
        _severities = d.pop("severities")
        for severities_item_data in _severities:
            severities_item = SeverityV1.from_dict(severities_item_data)

            severities.append(severities_item)

        severities_v1_list_response_body = cls(
            severities=severities,
        )

        severities_v1_list_response_body.additional_properties = d
        return severities_v1_list_response_body

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
