from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.audit_log_api_key_metadata_v2_response_body_api_key_roles_item import (
    AuditLogAPIKeyMetadataV2ResponseBodyApiKeyRolesItem,
)

T = TypeVar("T", bound="AuditLogAPIKeyMetadataV2ResponseBody")


@attr.s(auto_attribs=True)
class AuditLogAPIKeyMetadataV2ResponseBody:
    """
    Example:
        {'api_key_roles': ['incident_creator']}

    Attributes:
        api_key_roles (List[AuditLogAPIKeyMetadataV2ResponseBodyApiKeyRolesItem]): The roles that the API key has
            Example: ['incident_creator'].
    """

    api_key_roles: List[AuditLogAPIKeyMetadataV2ResponseBodyApiKeyRolesItem]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key_roles = []
        for api_key_roles_item_data in self.api_key_roles:
            api_key_roles_item = api_key_roles_item_data.value

            api_key_roles.append(api_key_roles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "api_key_roles": api_key_roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key_roles = []
        _api_key_roles = d.pop("api_key_roles")
        for api_key_roles_item_data in _api_key_roles:
            api_key_roles_item = AuditLogAPIKeyMetadataV2ResponseBodyApiKeyRolesItem(
                api_key_roles_item_data
            )

            api_key_roles.append(api_key_roles_item)

        audit_log_api_key_metadata_v2_response_body = cls(
            api_key_roles=api_key_roles,
        )

        audit_log_api_key_metadata_v2_response_body.additional_properties = d
        return audit_log_api_key_metadata_v2_response_body

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
