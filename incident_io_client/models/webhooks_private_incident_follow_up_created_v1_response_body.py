from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_private_incident_follow_up_created_v1_response_body_event_type import (
    WebhooksPrivateIncidentFollowUpCreatedV1ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.webhook_private_resource_v2_response_body import (
        WebhookPrivateResourceV2ResponseBody,
    )


T = TypeVar("T", bound="WebhooksPrivateIncidentFollowUpCreatedV1ResponseBody")


@_attrs_define
class WebhooksPrivateIncidentFollowUpCreatedV1ResponseBody:
    """
    Example:
        {'event_type': 'private_incident.follow_up_created_v1', 'private_incident.follow_up_created_v1': {'id':
            'abc123'}}

    Attributes:
        event_type (WebhooksPrivateIncidentFollowUpCreatedV1ResponseBodyEventType): What type of event is this webhook
            for? Example: private_incident.follow_up_created_v1.
        private_incident_follow_up_created_v1 (WebhookPrivateResourceV2ResponseBody):  Example: {'id': 'abc123'}.
    """

    event_type: WebhooksPrivateIncidentFollowUpCreatedV1ResponseBodyEventType
    private_incident_follow_up_created_v1: "WebhookPrivateResourceV2ResponseBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type.value

        private_incident_follow_up_created_v1 = (
            self.private_incident_follow_up_created_v1.to_dict()
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "private_incident.follow_up_created_v1": private_incident_follow_up_created_v1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_private_resource_v2_response_body import (
            WebhookPrivateResourceV2ResponseBody,
        )

        d = src_dict.copy()
        event_type = WebhooksPrivateIncidentFollowUpCreatedV1ResponseBodyEventType(
            d.pop("event_type")
        )

        private_incident_follow_up_created_v1 = WebhookPrivateResourceV2ResponseBody.from_dict(
            d.pop("private_incident.follow_up_created_v1")
        )

        webhooks_private_incident_follow_up_created_v1_response_body = cls(
            event_type=event_type,
            private_incident_follow_up_created_v1=private_incident_follow_up_created_v1,
        )

        webhooks_private_incident_follow_up_created_v1_response_body.additional_properties = d
        return webhooks_private_incident_follow_up_created_v1_response_body

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
