from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.incident_attachment_response_body import IncidentAttachmentResponseBody

T = TypeVar("T", bound="IncidentAttachmentsCreateResponseBody")


@attr.s(auto_attribs=True)
class IncidentAttachmentsCreateResponseBody:
    """
    Example:
        {'incident_attachment': {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'resource': {'external_id': '123', 'permalink': 'https://my.pagerduty.com/incidents/ABC', 'resource_type':
            'pager_duty_incident', 'title': 'The database has gone down'}}}

    Attributes:
        incident_attachment (IncidentAttachmentResponseBody):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYD5H',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'resource': {'external_id': '123', 'permalink':
            'https://my.pagerduty.com/incidents/ABC', 'resource_type': 'pager_duty_incident', 'title': 'The database has
            gone down'}}.
    """

    incident_attachment: IncidentAttachmentResponseBody
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
        incident_attachment = IncidentAttachmentResponseBody.from_dict(
            d.pop("incident_attachment")
        )

        incident_attachments_create_response_body = cls(
            incident_attachment=incident_attachment,
        )

        incident_attachments_create_response_body.additional_properties = d
        return incident_attachments_create_response_body

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
