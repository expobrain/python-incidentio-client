from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.returns_meta_v2_request_body import ReturnsMetaV2RequestBody


T = TypeVar("T", bound="ExpressionParseOptsPayloadV2RequestBody")


@_attrs_define
class ExpressionParseOptsPayloadV2RequestBody:
    """
    Example:
        {'returns': {'array': True, 'type': 'IncidentStatus'}, 'source': 'metadata.annotations["github.com/repo"]'}

    Attributes:
        returns (ReturnsMetaV2RequestBody):  Example: {'array': True, 'type': 'IncidentStatus'}.
        source (str): Source expression that is evaluated to a result Example: metadata.annotations["github.com/repo"].
    """

    returns: "ReturnsMetaV2RequestBody"
    source: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        returns = self.returns.to_dict()

        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "returns": returns,
                "source": source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.returns_meta_v2_request_body import ReturnsMetaV2RequestBody

        d = src_dict.copy()
        returns = ReturnsMetaV2RequestBody.from_dict(d.pop("returns"))

        source = d.pop("source")

        expression_parse_opts_payload_v2_request_body = cls(
            returns=returns,
            source=source,
        )

        expression_parse_opts_payload_v2_request_body.additional_properties = d
        return expression_parse_opts_payload_v2_request_body

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
