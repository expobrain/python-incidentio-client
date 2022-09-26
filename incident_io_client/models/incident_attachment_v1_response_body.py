from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.external_resource_v1_response_body import ExternalResourceV1ResponseBody

T = TypeVar("T", bound="IncidentAttachmentV1ResponseBody")


@attr.s(auto_attribs=True)
class IncidentAttachmentV1ResponseBody:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYD5H', 'incident_id': '01FCNDV6P870EA6S7TK1DSYD5H', 'resource': {'external_id':
            '123', 'permalink': 'https://my.pagerduty.com/incidents/ABC', 'resource_type': 'pager_duty_incident', 'title':
            'The database has gone down'}}

    Attributes:
        id (str): Unique identifier of this incident membership Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        incident_id (str): Unique identifier of the incident Example: 01FCNDV6P870EA6S7TK1DSYD5H.
        resource (ExternalResourceV1ResponseBody):  Example: {'external_id': '123', 'permalink':
            'https://my.pagerduty.com/incidents/ABC', 'resource_type': 'pager_duty_incident', 'title': 'The database has
            gone down'}.
    """

    id: str
    incident_id: str
    resource: ExternalResourceV1ResponseBody
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        incident_id = self.incident_id
        resource = self.resource.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "incident_id": incident_id,
                "resource": resource,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        incident_id = d.pop("incident_id")

        resource = ExternalResourceV1ResponseBody.from_dict(d.pop("resource"))

        incident_attachment_v1_response_body = cls(
            id=id,
            incident_id=incident_id,
            resource=resource,
        )

        incident_attachment_v1_response_body.additional_properties = d
        return incident_attachment_v1_response_body

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
