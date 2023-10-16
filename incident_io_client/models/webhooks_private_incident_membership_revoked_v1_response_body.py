from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_private_incident_membership_revoked_v1_response_body_event_type import (
    WebhooksPrivateIncidentMembershipRevokedV1ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.webhook_incident_user_v2_response_body import (
        WebhookIncidentUserV2ResponseBody,
    )


T = TypeVar("T", bound="WebhooksPrivateIncidentMembershipRevokedV1ResponseBody")


@_attrs_define
class WebhooksPrivateIncidentMembershipRevokedV1ResponseBody:
    """
    Example:
        {'event_type': 'private_incident.membership_revoked_v1', 'private_incident.membership_revoked_v1':
            {'actor_user_id': 'abc123', 'incident_id': 'abc123', 'user_id': 'abc123'}}

    Attributes:
        event_type (WebhooksPrivateIncidentMembershipRevokedV1ResponseBodyEventType): What type of event is this webhook
            for? Example: private_incident.membership_revoked_v1.
        private_incident_membership_revoked_v1 (WebhookIncidentUserV2ResponseBody):  Example: {'actor_user_id':
            'abc123', 'incident_id': 'abc123', 'user_id': 'abc123'}.
    """

    event_type: WebhooksPrivateIncidentMembershipRevokedV1ResponseBodyEventType
    private_incident_membership_revoked_v1: "WebhookIncidentUserV2ResponseBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type.value

        private_incident_membership_revoked_v1 = (
            self.private_incident_membership_revoked_v1.to_dict()
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "private_incident.membership_revoked_v1": private_incident_membership_revoked_v1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.webhook_incident_user_v2_response_body import (
            WebhookIncidentUserV2ResponseBody,
        )

        d = src_dict.copy()
        event_type = WebhooksPrivateIncidentMembershipRevokedV1ResponseBodyEventType(
            d.pop("event_type")
        )

        private_incident_membership_revoked_v1 = WebhookIncidentUserV2ResponseBody.from_dict(
            d.pop("private_incident.membership_revoked_v1")
        )

        webhooks_private_incident_membership_revoked_v1_response_body = cls(
            event_type=event_type,
            private_incident_membership_revoked_v1=private_incident_membership_revoked_v1,
        )

        webhooks_private_incident_membership_revoked_v1_response_body.additional_properties = d
        return webhooks_private_incident_membership_revoked_v1_response_body

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
