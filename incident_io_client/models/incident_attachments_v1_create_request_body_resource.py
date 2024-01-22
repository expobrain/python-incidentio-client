from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.incident_attachments_v1_create_request_body_resource_resource_type import (
    IncidentAttachmentsV1CreateRequestBodyResourceResourceType,
)

T = TypeVar("T", bound="IncidentAttachmentsV1CreateRequestBodyResource")


@_attrs_define
class IncidentAttachmentsV1CreateRequestBodyResource:
    """
    Example:
        {'external_id': '123', 'resource_type': 'pager_duty_incident'}

    Attributes:
        external_id (str): ID of the resource in the external system Example: 123.
        resource_type (IncidentAttachmentsV1CreateRequestBodyResourceResourceType): E.g. PagerDuty: the external system
            that holds the resource Example: pager_duty_incident.
    """

    external_id: str
    resource_type: IncidentAttachmentsV1CreateRequestBodyResourceResourceType
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_id = self.external_id

        resource_type = self.resource_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "resource_type": resource_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_id = d.pop("external_id")

        resource_type = IncidentAttachmentsV1CreateRequestBodyResourceResourceType(
            d.pop("resource_type")
        )

        incident_attachments_v1_create_request_body_resource = cls(
            external_id=external_id,
            resource_type=resource_type,
        )

        incident_attachments_v1_create_request_body_resource.additional_properties = d
        return incident_attachments_v1_create_request_body_resource

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
