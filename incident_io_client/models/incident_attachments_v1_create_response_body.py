from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.incident_attachment_v1_response_body import (
    IncidentAttachmentV1ResponseBody,
)

T = TypeVar("T", bound="IncidentAttachmentsV1CreateResponseBody")


@attr.s(auto_attribs=True)
class IncidentAttachmentsV1CreateResponseBody:
    """
    Example:
        {'incident_attachment': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'resource': {'external_id': '123', 'permalink': 'https://my.pagerduty.com/incidents/ABC', 'resource_type':
            'pager_duty_incident', 'title': 'The database has gone down'}}}

    Attributes:
        incident_attachment (IncidentAttachmentV1ResponseBody):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'resource': {'external_id': '123', 'permalink':
            'https://my.pagerduty.com/incidents/ABC', 'resource_type': 'pager_duty_incident', 'title': 'The database has
            gone down'}}.
    """

    incident_attachment: IncidentAttachmentV1ResponseBody
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_attachment = self.incident_attachment.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_attachment": incident_attachment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incident_attachment = IncidentAttachmentV1ResponseBody.from_dict(
            d.pop("incident_attachment")
        )

        incident_attachments_v1_create_response_body = cls(
            incident_attachment=incident_attachment,
        )

        incident_attachments_v1_create_response_body.additional_properties = d
        return incident_attachments_v1_create_response_body

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
