from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="AuditLogExternalResourceMetadataV2ResponseBody")


@attr.s(auto_attribs=True)
class AuditLogExternalResourceMetadataV2ResponseBody:
    """
    Example:
        {'external_id': 'q1234', 'resource_type': 'pager_duty_incident'}

    Attributes:
        external_id (str): The ID of the external resource in the 3rd party system Example: q1234.
        resource_type (str): The type of the external resource Example: pager_duty_incident.
    """

    external_id: str
    resource_type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_id = self.external_id
        resource_type = self.resource_type

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

        resource_type = d.pop("resource_type")

        audit_log_external_resource_metadata_v2_response_body = cls(
            external_id=external_id,
            resource_type=resource_type,
        )

        audit_log_external_resource_metadata_v2_response_body.additional_properties = d
        return audit_log_external_resource_metadata_v2_response_body

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
