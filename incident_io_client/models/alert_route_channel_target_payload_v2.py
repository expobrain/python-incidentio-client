from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.engine_param_binding_payload_v2 import EngineParamBindingPayloadV2


T = TypeVar("T", bound="AlertRouteChannelTargetPayloadV2")


@_attrs_define
class AlertRouteChannelTargetPayloadV2:
    """
    Example:
        {'binding': {'array_value': [{'literal': 'SEV123', 'reference': 'incident.severity'}], 'value': {'literal':
            'SEV123', 'reference': 'incident.severity'}}, 'channel_visibility': 'abc123'}

    Attributes:
        binding (EngineParamBindingPayloadV2):  Example: {'array_value': [{'literal': 'SEV123', 'reference':
            'incident.severity'}], 'value': {'literal': 'SEV123', 'reference': 'incident.severity'}}.
        channel_visibility (str): The visibility of the channel Example: abc123.
    """

    binding: "EngineParamBindingPayloadV2"
    channel_visibility: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        binding = self.binding.to_dict()

        channel_visibility = self.channel_visibility

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "binding": binding,
                "channel_visibility": channel_visibility,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.engine_param_binding_payload_v2 import EngineParamBindingPayloadV2

        d = src_dict.copy()
        binding = EngineParamBindingPayloadV2.from_dict(d.pop("binding"))

        channel_visibility = d.pop("channel_visibility")

        alert_route_channel_target_payload_v2 = cls(
            binding=binding,
            channel_visibility=channel_visibility,
        )

        alert_route_channel_target_payload_v2.additional_properties = d
        return alert_route_channel_target_payload_v2

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
