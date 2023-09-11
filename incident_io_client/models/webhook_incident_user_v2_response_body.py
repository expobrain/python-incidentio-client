from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="WebhookIncidentUserV2ResponseBody")


@attr.s(auto_attribs=True)
class WebhookIncidentUserV2ResponseBody:
    """
    Example:
        {'incident_id': 'abc123', 'user_id': 'abc123'}

    Attributes:
        incident_id (str): The ID of the incident Example: abc123.
        user_id (str): The ID of the user Example: abc123.
    """

    incident_id: str
    user_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        incident_id = self.incident_id
        user_id = self.user_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incident_id": incident_id,
                "user_id": user_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        incident_id = d.pop("incident_id")

        user_id = d.pop("user_id")

        webhook_incident_user_v2_response_body = cls(
            incident_id=incident_id,
            user_id=user_id,
        )

        webhook_incident_user_v2_response_body.additional_properties = d
        return webhook_incident_user_v2_response_body

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
