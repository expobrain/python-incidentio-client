from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MaintenanceWindowNotifyChannelV1")


@_attrs_define
class MaintenanceWindowNotifyChannelV1:
    """A channel that will receive notifications about this maintenance window

    Example:
        {'channel_id': 'C0ACTHQMHS8', 'channel_name': 'general', 'channel_type': 'public', 'is_private': False}

    Attributes:
        channel_id (str): The external provider channel ID (e.g. Slack channel ID) Example: C0ACTHQMHS8.
        channel_type (str): The type of channel (e.g. public, private) Example: public.
        channel_name (Union[Unset, str]): Human readable name of the channel Example: general.
        is_private (Union[Unset, bool]): Whether the channel is private
    """

    channel_id: str
    channel_type: str
    channel_name: Union[Unset, str] = UNSET
    is_private: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        channel_id = self.channel_id

        channel_type = self.channel_type

        channel_name = self.channel_name

        is_private = self.is_private

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "channel_type": channel_type,
            }
        )
        if channel_name is not UNSET:
            field_dict["channel_name"] = channel_name
        if is_private is not UNSET:
            field_dict["is_private"] = is_private

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        channel_id = d.pop("channel_id")

        channel_type = d.pop("channel_type")

        channel_name = d.pop("channel_name", UNSET)

        is_private = d.pop("is_private", UNSET)

        maintenance_window_notify_channel_v1 = cls(
            channel_id=channel_id,
            channel_type=channel_type,
            channel_name=channel_name,
            is_private=is_private,
        )

        maintenance_window_notify_channel_v1.additional_properties = d
        return maintenance_window_notify_channel_v1

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
