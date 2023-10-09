from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogUserRoleMembershipChangedMetadataV2ResponseBody")


@_attrs_define
class AuditLogUserRoleMembershipChangedMetadataV2ResponseBody:
    """
    Example:
        {'after_base_role_slug': 'owner', 'after_custom_role_slugs': 'engineering,data', 'before_base_role_slug':
            'admin', 'before_custom_role_slugs': 'engineering,security'}

    Attributes:
        after_base_role_slug (str): The base role slug of the user after their role memberships changed Example: owner.
        after_custom_role_slugs (str): The custom role slugs of the user after their role memberships changed, separated
            by commas Example: engineering,data.
        before_base_role_slug (str): The base role slug of the user before their role memberships changed Example:
            admin.
        before_custom_role_slugs (str): The custom role slugs of the user before their role memberships changed,
            separated by commas Example: engineering,security.
    """

    after_base_role_slug: str
    after_custom_role_slugs: str
    before_base_role_slug: str
    before_custom_role_slugs: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        after_base_role_slug = self.after_base_role_slug
        after_custom_role_slugs = self.after_custom_role_slugs
        before_base_role_slug = self.before_base_role_slug
        before_custom_role_slugs = self.before_custom_role_slugs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "after_base_role_slug": after_base_role_slug,
                "after_custom_role_slugs": after_custom_role_slugs,
                "before_base_role_slug": before_base_role_slug,
                "before_custom_role_slugs": before_custom_role_slugs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        after_base_role_slug = d.pop("after_base_role_slug")

        after_custom_role_slugs = d.pop("after_custom_role_slugs")

        before_base_role_slug = d.pop("before_base_role_slug")

        before_custom_role_slugs = d.pop("before_custom_role_slugs")

        audit_log_user_role_membership_changed_metadata_v2_response_body = cls(
            after_base_role_slug=after_base_role_slug,
            after_custom_role_slugs=after_custom_role_slugs,
            before_base_role_slug=before_base_role_slug,
            before_custom_role_slugs=before_custom_role_slugs,
        )

        audit_log_user_role_membership_changed_metadata_v2_response_body.additional_properties = d
        return audit_log_user_role_membership_changed_metadata_v2_response_body

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
