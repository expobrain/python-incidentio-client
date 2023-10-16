from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_status_v1_response_body import IncidentStatusV1ResponseBody


T = TypeVar("T", bound="IncidentStatusesV1ShowResponseBody")


@_attrs_define
class IncidentStatusesV1ShowResponseBody:
    """
    Example:
        {'incident_status': {'category': 'triage', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': "Impact
            has been **fully mitigated**, and we're ready to learn from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'name': 'Closed', 'rank': 4, 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        incident_status (IncidentStatusV1ResponseBody):  Example: {'category': 'triage', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': "Impact has been **fully mitigated**, and we're ready to learn
            from this incident.", 'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'name': 'Closed', 'rank': 4, 'updated_at':
            '2021-08-17T13:28:57.801578Z'}.
    """

    incident_status: "IncidentStatusV1ResponseBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_status = self.incident_status.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_status": incident_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.incident_status_v1_response_body import (
            IncidentStatusV1ResponseBody,
        )

        d = src_dict.copy()
        incident_status = IncidentStatusV1ResponseBody.from_dict(d.pop("incident_status"))

        incident_statuses_v1_show_response_body = cls(
            incident_status=incident_status,
        )

        incident_statuses_v1_show_response_body.additional_properties = d
        return incident_statuses_v1_show_response_body

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
