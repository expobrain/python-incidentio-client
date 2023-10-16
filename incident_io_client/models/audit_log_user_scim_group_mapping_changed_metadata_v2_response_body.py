from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogUserSCIMGroupMappingChangedMetadataV2ResponseBody")


@_attrs_define
class AuditLogUserSCIMGroupMappingChangedMetadataV2ResponseBody:
    """
    Example:
        {'after_base_role_slug': 'owner', 'after_custom_role_slugs': 'engineering,data', 'before_base_role_slug':
            'admin', 'before_custom_role_slugs': 'engineering,security'}

    Attributes:
        after_base_role_slug (Union[Unset, str]): The base role slug of this SCIM group after the mapping was changed
            (if any) Example: owner.
        after_custom_role_slugs (Union[Unset, str]): The custom role slugs of this SCIM group after the mapping was
            changed (if any), separated by commas Example: engineering,data.
        before_base_role_slug (Union[Unset, str]): The base role slug assigned to this SCIM group before the mapping was
            changed (if any) Example: admin.
        before_custom_role_slugs (Union[Unset, str]): The custom role slugs of this SCIM group before the mapping was
            changed (if any), separated by commas Example: engineering,security.
    """

    after_base_role_slug: Union[Unset, str] = UNSET
    after_custom_role_slugs: Union[Unset, str] = UNSET
    before_base_role_slug: Union[Unset, str] = UNSET
    before_custom_role_slugs: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        after_base_role_slug = self.after_base_role_slug
        after_custom_role_slugs = self.after_custom_role_slugs
        before_base_role_slug = self.before_base_role_slug
        before_custom_role_slugs = self.before_custom_role_slugs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after_base_role_slug is not UNSET:
            field_dict["after_base_role_slug"] = after_base_role_slug
        if after_custom_role_slugs is not UNSET:
            field_dict["after_custom_role_slugs"] = after_custom_role_slugs
        if before_base_role_slug is not UNSET:
            field_dict["before_base_role_slug"] = before_base_role_slug
        if before_custom_role_slugs is not UNSET:
            field_dict["before_custom_role_slugs"] = before_custom_role_slugs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        after_base_role_slug = d.pop("after_base_role_slug", UNSET)

        after_custom_role_slugs = d.pop("after_custom_role_slugs", UNSET)

        before_base_role_slug = d.pop("before_base_role_slug", UNSET)

        before_custom_role_slugs = d.pop("before_custom_role_slugs", UNSET)

        audit_log_user_scim_group_mapping_changed_metadata_v2_response_body = cls(
            after_base_role_slug=after_base_role_slug,
            after_custom_role_slugs=after_custom_role_slugs,
            before_base_role_slug=before_base_role_slug,
            before_custom_role_slugs=before_custom_role_slugs,
        )

        audit_log_user_scim_group_mapping_changed_metadata_v2_response_body.additional_properties = (
            d
        )
        return audit_log_user_scim_group_mapping_changed_metadata_v2_response_body

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
