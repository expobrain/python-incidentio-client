import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.action_v1_status import ActionV1Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.external_issue_reference_v1 import ExternalIssueReferenceV1
    from ..models.user_v1 import UserV1


T = TypeVar("T", bound="ActionV1")


@_attrs_define
class ActionV1:
    """
    Example:
        {'assignee': {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Lisa Karlin Curtis',
            'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}, 'completed_at': '2021-08-17T13:28:57.801578Z', 'created_at':
            '2021-08-17T13:28:57.801578Z', 'description': 'Call the fire brigade', 'external_issue_reference':
            {'issue_name': 'INC-123', 'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-
            write-up', 'provider': 'asana'}, 'follow_up': True, 'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'incident_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'status': 'outstanding', 'updated_at': '2021-08-17T13:28:57.801578Z'}

    Attributes:
        created_at (datetime.datetime): When the action was created Example: 2021-08-17T13:28:57.801578Z.
        follow_up (bool): Whether an action is marked as follow-up Example: True.
        id (str): Unique identifier for the action Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        incident_id (str): Unique identifier of the incident the action belongs to Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        status (ActionV1Status): Status of the action Example: outstanding.
        updated_at (datetime.datetime): When the action was last updated Example: 2021-08-17T13:28:57.801578Z.
        assignee (Union[Unset, UserV1]):  Example: {'email': 'lisa@incident.io', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'name': 'Lisa Karlin Curtis', 'role': 'viewer', 'slack_user_id': 'U02AYNF2XJM'}.
        completed_at (Union[Unset, datetime.datetime]): When the action was completed Example:
            2021-08-17T13:28:57.801578Z.
        description (Union[Unset, str]): Description of the action Example: Call the fire brigade.
        external_issue_reference (Union[Unset, ExternalIssueReferenceV1]):  Example: {'issue_name': 'INC-123',
            'issue_permalink': 'https://linear.app/incident-io/issue/INC-1609/find-copywriter-to-write-up', 'provider':
            'asana'}.
    """

    created_at: datetime.datetime
    follow_up: bool
    id: str
    incident_id: str
    status: ActionV1Status
    updated_at: datetime.datetime
    assignee: Union[Unset, "UserV1"] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    external_issue_reference: Union[Unset, "ExternalIssueReferenceV1"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        follow_up = self.follow_up

        id = self.id

        incident_id = self.incident_id

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        assignee: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.assignee, Unset):
            assignee = self.assignee.to_dict()

        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        description = self.description

        external_issue_reference: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_issue_reference, Unset):
            external_issue_reference = self.external_issue_reference.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "follow_up": follow_up,
                "id": id,
                "incident_id": incident_id,
                "status": status,
                "updated_at": updated_at,
            }
        )
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if description is not UNSET:
            field_dict["description"] = description
        if external_issue_reference is not UNSET:
            field_dict["external_issue_reference"] = external_issue_reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.external_issue_reference_v1 import ExternalIssueReferenceV1
        from ..models.user_v1 import UserV1

        d = src_dict.copy()
        created_at = isoparse(d.pop("created_at"))

        follow_up = d.pop("follow_up")

        id = d.pop("id")

        incident_id = d.pop("incident_id")

        status = ActionV1Status(d.pop("status"))

        updated_at = isoparse(d.pop("updated_at"))

        _assignee = d.pop("assignee", UNSET)
        assignee: Union[Unset, UserV1]
        if isinstance(_assignee, Unset):
            assignee = UNSET
        else:
            assignee = UserV1.from_dict(_assignee)

        _completed_at = d.pop("completed_at", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        description = d.pop("description", UNSET)

        _external_issue_reference = d.pop("external_issue_reference", UNSET)
        external_issue_reference: Union[Unset, ExternalIssueReferenceV1]
        if isinstance(_external_issue_reference, Unset):
            external_issue_reference = UNSET
        else:
            external_issue_reference = ExternalIssueReferenceV1.from_dict(
                _external_issue_reference
            )

        action_v1 = cls(
            created_at=created_at,
            follow_up=follow_up,
            id=id,
            incident_id=incident_id,
            status=status,
            updated_at=updated_at,
            assignee=assignee,
            completed_at=completed_at,
            description=description,
            external_issue_reference=external_issue_reference,
        )

        action_v1.additional_properties = d
        return action_v1

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
