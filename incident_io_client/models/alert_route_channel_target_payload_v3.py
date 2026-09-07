from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.alert_route_channel_target_payload_v3_channel_visibility import (
    AlertRouteChannelTargetPayloadV3ChannelVisibility,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3


T = TypeVar("T", bound="AlertRouteChannelTargetPayloadV3")


@_attrs_define
class AlertRouteChannelTargetPayloadV3:
    """
    Example:
        {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility': 'public', 'group_alerts_summary': False}

    Attributes:
        binding (EngineParamBindingPayloadV3):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        channel_visibility (AlertRouteChannelTargetPayloadV3ChannelVisibility): The visibility of the channel Example:
            public.
        group_alerts_summary (Union[Unset, bool]): Whether grouped alerts should render as a single group-summary
            message per channel
    """

    binding: "EngineParamBindingPayloadV3"
    channel_visibility: AlertRouteChannelTargetPayloadV3ChannelVisibility
    group_alerts_summary: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        binding = self.binding.to_dict()

        channel_visibility = self.channel_visibility.value

        group_alerts_summary = self.group_alerts_summary

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "binding": binding,
                "channel_visibility": channel_visibility,
            }
        )
        if group_alerts_summary is not UNSET:
            field_dict["group_alerts_summary"] = group_alerts_summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.engine_param_binding_payload_v3 import EngineParamBindingPayloadV3

        d = src_dict.copy()
        binding = EngineParamBindingPayloadV3.from_dict(d.pop("binding"))

        channel_visibility = AlertRouteChannelTargetPayloadV3ChannelVisibility(
            d.pop("channel_visibility")
        )

        group_alerts_summary = d.pop("group_alerts_summary", UNSET)

        alert_route_channel_target_payload_v3 = cls(
            binding=binding,
            channel_visibility=channel_visibility,
            group_alerts_summary=group_alerts_summary,
        )

        alert_route_channel_target_payload_v3.additional_properties = d
        return alert_route_channel_target_payload_v3

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
