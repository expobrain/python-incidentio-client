from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhooks_public_incident_action_created_v1_response_body_event_type import (
    WebhooksPublicIncidentActionCreatedV1ResponseBodyEventType,
)

if TYPE_CHECKING:
    from ..models.action_v1_response_body import ActionV1ResponseBody


T = TypeVar("T", bound="WebhooksPublicIncidentActionCreatedV1ResponseBody")


@_attrs_define
class WebhooksPublicIncidentActionCreatedV1ResponseBody:
    """
    Example:
        {'event_type': 'public_incident.action_created_v1', 'public_incident.action_created_v1': {'assignee': {'email':
            'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer',
            'slack_user_id': 'U02AYNF2XJM'}, 'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Call the fire brigade', 'external_issue_reference':
            {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'asana'}, 'follow_up': True, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'status': 'outstanding', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        event_type (WebhooksPublicIncidentActionCreatedV1ResponseBodyEventType): What type of event is this webhook for?
            Example: public_incident.action_created_v1.
        public_incident_action_created_v1 (ActionV1ResponseBody):  Example: {'assignee': {'email': 'lisa@incident.io',
            'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id':
            'U02AYNF2XJM'}, 'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z',
            'description': 'Call the fire brigade', 'external_issue_reference': {'issue_name': 'INC-123', 'issue_permalink':
            'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up', 'provider': 'asana'}, 'follow_up':
            True, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'status': 'outstanding',
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    event_type: WebhooksPublicIncidentActionCreatedV1ResponseBodyEventType
    public_incident_action_created_v1: "ActionV1ResponseBody"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_type = self.event_type.value

        public_incident_action_created_v1 = self.public_incident_action_created_v1.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "public_incident.action_created_v1": public_incident_action_created_v1,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_v1_response_body import ActionV1ResponseBody

        d = src_dict.copy()
        event_type = WebhooksPublicIncidentActionCreatedV1ResponseBodyEventType(
            d.pop("event_type")
        )

        public_incident_action_created_v1 = ActionV1ResponseBody.from_dict(
            d.pop("public_incident.action_created_v1")
        )

        webhooks_public_incident_action_created_v1_response_body = cls(
            event_type=event_type,
            public_incident_action_created_v1=public_incident_action_created_v1,
        )

        webhooks_public_incident_action_created_v1_response_body.additional_properties = d
        return webhooks_public_incident_action_created_v1_response_body

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
