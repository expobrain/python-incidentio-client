from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuditLogUserLoggedInMetadataV2")


@_attrs_define
class AuditLogUserLoggedInMetadataV2:
    """
    Example:
        {'login_method': 'slack_oidc'}

    Attributes:
        login_method (str): The method the user authenticated with Example: slack_oidc.
    """

    login_method: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        login_method = self.login_method

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login_method": login_method,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        login_method = d.pop("login_method")

        audit_log_user_logged_in_metadata_v2 = cls(
            login_method=login_method,
        )

        audit_log_user_logged_in_metadata_v2.additional_properties = d
        return audit_log_user_logged_in_metadata_v2

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
