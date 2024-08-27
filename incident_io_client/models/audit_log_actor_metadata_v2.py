from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogActorMetadataV2")


@_attrs_define
class AuditLogActorMetadataV2:
    """
    Example:
        {'api_key_roles': 'abc123', 'external_resource_external_id': 'q1234', 'external_resource_type':
            'pager_duty_incident', 'user_base_role_slug': 'admin', 'user_custom_role_slugs': 'engineering,security'}

    Attributes:
        api_key_roles (Union[Unset, str]): The roles that the API key has, separated by commas (if it's an API key
            actor) Example: abc123.
        external_resource_external_id (Union[Unset, str]): The ID of the external resource in the 3rd party system (if
            it's an external resource actor) Example: q1234.
        external_resource_type (Union[Unset, str]): The type of the external resource (if it's an external resource
            actor) Example: pager_duty_incident.
        user_base_role_slug (Union[Unset, str]): The base role slug of the user (if it's a user actor) Example: admin.
        user_custom_role_slugs (Union[Unset, str]): The custom role slugs of the user, separated by commas (if it's a
            user actor) Example: engineering,security.
    """

    api_key_roles: Union[Unset, str] = UNSET
    external_resource_external_id: Union[Unset, str] = UNSET
    external_resource_type: Union[Unset, str] = UNSET
    user_base_role_slug: Union[Unset, str] = UNSET
    user_custom_role_slugs: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key_roles = self.api_key_roles

        external_resource_external_id = self.external_resource_external_id

        external_resource_type = self.external_resource_type

        user_base_role_slug = self.user_base_role_slug

        user_custom_role_slugs = self.user_custom_role_slugs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key_roles is not UNSET:
            field_dict["api_key_roles"] = api_key_roles
        if external_resource_external_id is not UNSET:
            field_dict["external_resource_external_id"] = external_resource_external_id
        if external_resource_type is not UNSET:
            field_dict["external_resource_type"] = external_resource_type
        if user_base_role_slug is not UNSET:
            field_dict["user_base_role_slug"] = user_base_role_slug
        if user_custom_role_slugs is not UNSET:
            field_dict["user_custom_role_slugs"] = user_custom_role_slugs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        api_key_roles = d.pop("api_key_roles", UNSET)

        external_resource_external_id = d.pop("external_resource_external_id", UNSET)

        external_resource_type = d.pop("external_resource_type", UNSET)

        user_base_role_slug = d.pop("user_base_role_slug", UNSET)

        user_custom_role_slugs = d.pop("user_custom_role_slugs", UNSET)

        audit_log_actor_metadata_v2 = cls(
            api_key_roles=api_key_roles,
            external_resource_external_id=external_resource_external_id,
            external_resource_type=external_resource_type,
            user_base_role_slug=user_base_role_slug,
            user_custom_role_slugs=user_custom_role_slugs,
        )

        audit_log_actor_metadata_v2.additional_properties = d
        return audit_log_actor_metadata_v2

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
