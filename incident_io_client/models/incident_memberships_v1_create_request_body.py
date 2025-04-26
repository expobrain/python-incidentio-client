from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IncidentMembershipsV1CreateRequestBody")


@_attrs_define
class IncidentMembershipsV1CreateRequestBody:
    """
    Example:
        {'incident_id': '01ET65M7ZADYFCKD4K1AE2QNMC', 'user_id': '01FCQSP07Z74QMMYPDDGQB9FTG'}

    Attributes:
        incident_id (str):  Example: 01ET65M7ZADYFCKD4K1AE2QNMC.
        user_id (str):  Example: 01FCQSP07Z74QMMYPDDGQB9FTG.
    """

    incident_id: str
    user_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_id = self.incident_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incident_id = d.pop("incident_id")

        user_id = d.pop("user_id")

        incident_memberships_v1_create_request_body = cls(
            incident_id=incident_id,
            user_id=user_id,
        )

        incident_memberships_v1_create_request_body.additional_properties = d
        return incident_memberships_v1_create_request_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
