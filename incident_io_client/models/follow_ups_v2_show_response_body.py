from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.follow_up_v2 import FollowUpV2


T = TypeVar("T", bound="FollowUpsV2ShowResponseBody")


@_attrs_define
class FollowUpsV2ShowResponseBody:
    """
    Example:
        {'follow_up': {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa
            Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'completed_at':
            '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Call the fire
            brigade', 'external_issue_reference': {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-
            io/issue/INC-1609/find-copywriter-to-write-up', 'provider': 'asana'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'priority': {'description': 'A follow-up that requires immediate
            attention.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Urgent', 'rank': 10}, 'status': 'outstanding',
            'title': 'Cat is stuck in the tree', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        follow_up (FollowUpV2):  Example: {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'completed_at':
            '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Call the fire
            brigade', 'external_issue_reference': {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-
            io/issue/INC-1609/find-copywriter-to-write-up', 'provider': 'asana'}, 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'priority': {'description': 'A follow-up that requires immediate
            attention.', 'id': '01GNW4BAQ7XRMFF6FHKNXDFPRW', 'name': 'Urgent', 'rank': 10}, 'status': 'outstanding',
            'title': 'Cat is stuck in the tree', 'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    follow_up: "FollowUpV2"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        follow_up = self.follow_up.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "follow_up": follow_up,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.follow_up_v2 import FollowUpV2

        d = src_dict.copy()
        follow_up = FollowUpV2.from_dict(d.pop("follow_up"))

        follow_ups_v2_show_response_body = cls(
            follow_up=follow_up,
        )

        follow_ups_v2_show_response_body.additional_properties = d
        return follow_ups_v2_show_response_body

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
