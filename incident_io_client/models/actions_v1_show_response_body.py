from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.action_v1_response_body import ActionV1ResponseBody


T = TypeVar("T", bound="ActionsV1ShowResponseBody")


@attr.s(auto_attribs=True)
class ActionsV1ShowResponseBody:
    """
    Example:
        {'action': {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin
            Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'completed_at': '2021-08-17T13:28:57.801578Z',
            'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Call the fire brigade', 'external_issue_reference':
            {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'asana'}, 'follow_up': True, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'status': 'outstanding', 'updated_at': '2021-08-17T13:28:57.801578Z'}}

    Attributes:
        action (ActionV1ResponseBody):  Example: {'assignee': {'email': 'lisa@incident.io', 'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'},
            'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at': '2021-08-17T13:28:57.801578Z', 'description': 'Call
            the fire brigade', 'external_issue_reference': {'issue_name': 'INC-123', 'issue_permalink':
            'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up', 'provider': 'asana'}, 'follow_up':
            True, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'status': 'outstanding',
            'updated_at': '2021-08-17T13:28:57.801578Z'}.
    """

    action: "ActionV1ResponseBody"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.action_v1_response_body import ActionV1ResponseBody

        d = src_dict.copy()
        action = ActionV1ResponseBody.from_dict(d.pop("action"))

        actions_v1_show_response_body = cls(
            action=action,
        )

        actions_v1_show_response_body.additional_properties = d
        return actions_v1_show_response_body

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
