from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.incident_status_v1_response_body import IncidentStatusV1ResponseBody


T = TypeVar("T", bound="IncidentStatusesV1ListResponseBody")


@attr.s(auto_attribs=True)
class IncidentStatusesV1ListResponseBody:
    """
    Example:
        {'incident_statuses': [{'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description':
            "Impact has been **fully mitigated**, and we're ready to learn from this incident.", 'id':
            '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'}]}

    Attributes:
        incident_statuses (List['IncidentStatusV1ResponseBody']):  Example: [{'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}].
    """

    incident_statuses: List["IncidentStatusV1ResponseBody"]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_statuses = []
        for incident_statuses_item_data in self.incident_statuses:
            incident_statuses_item = incident_statuses_item_data.to_dict()

            incident_statuses.append(incident_statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_statuses": incident_statuses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.incident_status_v1_response_body import (
            IncidentStatusV1ResponseBody,
        )

        d = src_dict.copy()
        incident_statuses = []
        _incident_statuses = d.pop("incident_statuses")
        for incident_statuses_item_data in _incident_statuses:
            incident_statuses_item = IncidentStatusV1ResponseBody.from_dict(
                incident_statuses_item_data
            )

            incident_statuses.append(incident_statuses_item)

        incident_statuses_v1_list_response_body = cls(
            incident_statuses=incident_statuses,
        )

        incident_statuses_v1_list_response_body.additional_properties = d
        return incident_statuses_v1_list_response_body

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
