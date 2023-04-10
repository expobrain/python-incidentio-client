from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="AuditLogUserMetadataV2ResponseBody")


@attr.s(auto_attribs=True)
class AuditLogUserMetadataV2ResponseBody:
    """
    Example:
        {'base_role_slug': 'admin', 'custom_role_slugs': ['engineering']}

    Attributes:
        base_role_slug (str): The base role slug of the user Example: admin.
        custom_role_slugs (List[str]): The custom role slugs of the user Example: ['engineering'].
    """

    base_role_slug: str
    custom_role_slugs: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base_role_slug = self.base_role_slug
        custom_role_slugs = self.custom_role_slugs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_role_slug": base_role_slug,
                "custom_role_slugs": custom_role_slugs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base_role_slug = d.pop("base_role_slug")

        custom_role_slugs = cast(List[str], d.pop("custom_role_slugs"))

        audit_log_user_metadata_v2_response_body = cls(
            base_role_slug=base_role_slug,
            custom_role_slugs=custom_role_slugs,
        )

        audit_log_user_metadata_v2_response_body.additional_properties = d
        return audit_log_user_metadata_v2_response_body

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
