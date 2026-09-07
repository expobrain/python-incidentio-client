import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ip_allowlist_item_v1 import IPAllowlistItemV1


T = TypeVar("T", bound="IPAllowlistV1")


@_attrs_define
class IPAllowlistV1:
    """
    Example:
        {'allowlist': [{'label': 'London HQ', 'value': '192.0.2.0'}], 'enabled': True, 'updated_at':
            '2021-08-17T13:28:57.801578Z', 'version': 1}

    Attributes:
        allowlist (List['IPAllowlistItemV1']): A list of IP addresses or CIDR prefixes to allow Example: [{'label':
            'London HQ', 'value': '192.0.2.0'}].
        enabled (bool): Whether this IP allowlist is enabled or not Example: True.
        version (int): The version of this IP allowlist Example: 1.
        updated_at (Union[Unset, datetime.datetime]): The time this allowlist was last updated Example:
            2021-08-17T13:28:57.801578Z.
    """

    allowlist: List["IPAllowlistItemV1"]
    enabled: bool
    version: int
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowlist = []
        for allowlist_item_data in self.allowlist:
            allowlist_item = allowlist_item_data.to_dict()
            allowlist.append(allowlist_item)

        enabled = self.enabled

        version = self.version

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allowlist": allowlist,
                "enabled": enabled,
                "version": version,
            }
        )
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ip_allowlist_item_v1 import IPAllowlistItemV1

        d = src_dict.copy()
        allowlist = []
        _allowlist = d.pop("allowlist")
        for allowlist_item_data in _allowlist:
            allowlist_item = IPAllowlistItemV1.from_dict(allowlist_item_data)

            allowlist.append(allowlist_item)

        enabled = d.pop("enabled")

        version = d.pop("version")

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        ip_allowlist_v1 = cls(
            allowlist=allowlist,
            enabled=enabled,
            version=version,
            updated_at=updated_at,
        )

        ip_allowlist_v1.additional_properties = d
        return ip_allowlist_v1

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
