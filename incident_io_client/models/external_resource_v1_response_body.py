from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.external_resource_v1_response_body_resource_type import (
    ExternalResourceV1ResponseBodyResourceType,
)

T = TypeVar("T", bound="ExternalResourceV1ResponseBody")


@attr.s(auto_attribs=True)
class ExternalResourceV1ResponseBody:
    """
    Example:
        {'external_id': '123', 'permalink': 'https://my.pagerduty.com/incidents/ABC', 'resource_type':
            'pager_duty_incident', 'title': 'The database has gone down'}

    Attributes:
        external_id (str): ID of the resource in the external system Example: 123.
        permalink (str): URL of the resource Example: https://my.pagerduty.com/incidents/ABC.
        resource_type (ExternalResourceV1ResponseBodyResourceType): E.g. PagerDuty: the external system that holds the
            resource Example: pager_duty_incident.
        title (str): Title of resource Example: The database has gone down.
    """

    external_id: str
    permalink: str
    resource_type: ExternalResourceV1ResponseBodyResourceType
    title: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_id = self.external_id
        permalink = self.permalink
        resource_type = self.resource_type.value

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "external_id": external_id,
                "permalink": permalink,
                "resource_type": resource_type,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_id = d.pop("external_id")

        permalink = d.pop("permalink")

        resource_type = ExternalResourceV1ResponseBodyResourceType(d.pop("resource_type"))

        title = d.pop("title")

        external_resource_v1_response_body = cls(
            external_id=external_id,
            permalink=permalink,
            resource_type=resource_type,
            title=title,
        )

        external_resource_v1_response_body.additional_properties = d
        return external_resource_v1_response_body

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
