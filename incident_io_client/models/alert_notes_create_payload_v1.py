from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertNotesCreatePayloadV1")


@_attrs_define
class AlertNotesCreatePayloadV1:
    r"""
    Example:
        {'alert_group_id': '01HB9Z8WANK6P870EA6S7TK1DS', 'alert_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'content': 'Customer
            reports **checkout 500s** starting ~14:32 UTC. Investigating `payments-api`.\n\n- Error rate: ~12% on
            `/checkout`\n- Region: `eu-west-1`\n- See [dashboard](https://grafana.example.com/d/abc)\n'}

    Attributes:
        content (str): Markdown body of the note Example: Customer reports **checkout 500s** starting ~14:32 UTC.
            Investigating `payments-api`.

            - Error rate: ~12% on `/checkout`
            - Region: `eu-west-1`
            - See [dashboard](https://grafana.example.com/d/abc)
            .
        alert_group_id (Union[Unset, str]): ID of the alert group to add the note to. Provide exactly one of alert_id or
            alert_group_id. Example: 01HB9Z8WANK6P870EA6S7TK1DS.
        alert_id (Union[Unset, str]): ID of the alert to add the note to. Provide exactly one of alert_id or
            alert_group_id. Example: 01FCNDV6P870EA6S7TK1DSYDG0.
    """

    content: str
    alert_group_id: Union[Unset, str] = UNSET
    alert_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content

        alert_group_id = self.alert_group_id

        alert_id = self.alert_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if alert_group_id is not UNSET:
            field_dict["alert_group_id"] = alert_group_id
        if alert_id is not UNSET:
            field_dict["alert_id"] = alert_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        alert_group_id = d.pop("alert_group_id", UNSET)

        alert_id = d.pop("alert_id", UNSET)

        alert_notes_create_payload_v1 = cls(
            content=content,
            alert_group_id=alert_group_id,
            alert_id=alert_id,
        )

        alert_notes_create_payload_v1.additional_properties = d
        return alert_notes_create_payload_v1

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
