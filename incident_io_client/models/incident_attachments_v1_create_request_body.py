from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_attachments_v1_create_request_body_resource import (
        IncidentAttachmentsV1CreateRequestBodyResource,
    )


T = TypeVar("T", bound="IncidentAttachmentsV1CreateRequestBody")


@_attrs_define
class IncidentAttachmentsV1CreateRequestBody:
    """
    Example:
        {'incident_id': '01FDAG4SAP5TYPT98WGR2N7W91', 'resource': {'external_id': '123', 'resource_type':
            'pager_duty_incident'}}

    Attributes:
        incident_id (str): ID of the incident to add an attachment to Example: 01FDAG4SAP5TYPT98WGR2N7W91.
        resource (IncidentAttachmentsV1CreateRequestBodyResource):  Example: {'external_id': '123', 'resource_type':
            'pager_duty_incident'}.
    """

    incident_id: str
    resource: "IncidentAttachmentsV1CreateRequestBodyResource"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_id = self.incident_id

        resource = self.resource.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "resource": resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.incident_attachments_v1_create_request_body_resource import (
            IncidentAttachmentsV1CreateRequestBodyResource,
        )

        d = src_dict.copy()
        incident_id = d.pop("incident_id")

        resource = IncidentAttachmentsV1CreateRequestBodyResource.from_dict(d.pop("resource"))

        incident_attachments_v1_create_request_body = cls(
            incident_id=incident_id,
            resource=resource,
        )

        incident_attachments_v1_create_request_body.additional_properties = d
        return incident_attachments_v1_create_request_body

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
