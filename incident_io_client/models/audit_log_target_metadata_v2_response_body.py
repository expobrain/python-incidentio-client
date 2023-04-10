from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.audit_log_target_metadata_v2_response_body_api_key_roles_item import (
    AuditLogTargetMetadataV2ResponseBodyApiKeyRolesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogTargetMetadataV2ResponseBody")


@attr.s(auto_attribs=True)
class AuditLogTargetMetadataV2ResponseBody:
    """
    Example:
        {'api_key_roles': ['incident_creator'], 'base_role_slug': 'admin', 'custom_role_slugs': ['engineering']}

    Attributes:
        api_key_roles (Union[Unset, List[AuditLogTargetMetadataV2ResponseBodyApiKeyRolesItem]]): The roles that the API
            key has (if it's an API Key actor) Example: ['incident_creator'].
        base_role_slug (Union[Unset, str]): The base role slug of the user (if it's a user actor) Example: admin.
        custom_role_slugs (Union[Unset, List[str]]): The custom role slugs of the user (if it's a user actor) Example:
            ['engineering'].
    """

    api_key_roles: Union[Unset, List[AuditLogTargetMetadataV2ResponseBodyApiKeyRolesItem]] = UNSET
    base_role_slug: Union[Unset, str] = UNSET
    custom_role_slugs: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key_roles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.api_key_roles, Unset):
            api_key_roles = []
            for api_key_roles_item_data in self.api_key_roles:
                api_key_roles_item = api_key_roles_item_data.value

                api_key_roles.append(api_key_roles_item)

        base_role_slug = self.base_role_slug
        custom_role_slugs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.custom_role_slugs, Unset):
            custom_role_slugs = self.custom_role_slugs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key_roles is not UNSET:
            field_dict["api_key_roles"] = api_key_roles
        if base_role_slug is not UNSET:
            field_dict["base_role_slug"] = base_role_slug
        if custom_role_slugs is not UNSET:
            field_dict["custom_role_slugs"] = custom_role_slugs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key_roles = []
        _api_key_roles = d.pop("api_key_roles", UNSET)
        for api_key_roles_item_data in _api_key_roles or []:
            api_key_roles_item = AuditLogTargetMetadataV2ResponseBodyApiKeyRolesItem(
                api_key_roles_item_data
            )

            api_key_roles.append(api_key_roles_item)

        base_role_slug = d.pop("base_role_slug", UNSET)

        custom_role_slugs = cast(List[str], d.pop("custom_role_slugs", UNSET))

        audit_log_target_metadata_v2_response_body = cls(
            api_key_roles=api_key_roles,
            base_role_slug=base_role_slug,
            custom_role_slugs=custom_role_slugs,
        )

        audit_log_target_metadata_v2_response_body.additional_properties = d
        return audit_log_target_metadata_v2_response_body

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
