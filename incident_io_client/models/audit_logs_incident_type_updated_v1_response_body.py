import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.audit_log_actor_v2_response_body import AuditLogActorV2ResponseBody
    from ..models.audit_log_entry_context_v2_response_body import (
        AuditLogEntryContextV2ResponseBody,
    )
    from ..models.audit_log_target_v2_response_body import AuditLogTargetV2ResponseBody


T = TypeVar("T", bound="AuditLogsIncidentTypeUpdatedV1ResponseBody")


@_attrs_define
class AuditLogsIncidentTypeUpdatedV1ResponseBody:
    """
    Example:
        {'action': 'incident_type.updated', 'actor': {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'metadata':
            {'user_base_role_slug': 'admin', 'user_custom_role_slugs': 'engineering,security'}, 'name': 'John Doe', 'type':
            'user'}, 'context': {'location': '1.2.3.4', 'user_agent': 'Chrome/91.0.4472.114'}, 'occurred_at':
            '2021-08-17T13:28:57.801578Z', 'targets': [{'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Security', 'type':
            'incident_type'}], 'version': 1}

    Attributes:
        action (str): The type of log entry that this is Example: incident_type.updated.
        actor (AuditLogActorV2ResponseBody):  Example: {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'metadata':
            {'user_base_role_slug': 'admin', 'user_custom_role_slugs': 'engineering,security'}, 'name': 'John Doe', 'type':
            'user'}.
        context (AuditLogEntryContextV2ResponseBody):  Example: {'location': '1.2.3.4', 'user_agent':
            'Chrome/91.0.4472.114'}.
        occurred_at (datetime.datetime): When the entry occurred Example: 2021-08-17T13:28:57.801578Z.
        targets (List['AuditLogTargetV2ResponseBody']): The custom field that was created Example: [{'id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'name': 'Security', 'type': 'incident_type'}].
        version (int): Which version the event is Example: 1.
    """

    action: str
    actor: "AuditLogActorV2ResponseBody"
    context: "AuditLogEntryContextV2ResponseBody"
    occurred_at: datetime.datetime
    targets: List["AuditLogTargetV2ResponseBody"]
    version: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action
        actor = self.actor.to_dict()

        context = self.context.to_dict()

        occurred_at = self.occurred_at.isoformat()

        targets = []
        for targets_item_data in self.targets:
            targets_item = targets_item_data.to_dict()

            targets.append(targets_item)

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "actor": actor,
                "context": context,
                "occurred_at": occurred_at,
                "targets": targets,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.audit_log_actor_v2_response_body import (
            AuditLogActorV2ResponseBody,
        )
        from ..models.audit_log_entry_context_v2_response_body import (
            AuditLogEntryContextV2ResponseBody,
        )
        from ..models.audit_log_target_v2_response_body import (
            AuditLogTargetV2ResponseBody,
        )

        d = src_dict.copy()
        action = d.pop("action")

        actor = AuditLogActorV2ResponseBody.from_dict(d.pop("actor"))

        context = AuditLogEntryContextV2ResponseBody.from_dict(d.pop("context"))

        occurred_at = isoparse(d.pop("occurred_at"))

        targets = []
        _targets = d.pop("targets")
        for targets_item_data in _targets:
            targets_item = AuditLogTargetV2ResponseBody.from_dict(targets_item_data)

            targets.append(targets_item)

        version = d.pop("version")

        audit_logs_incident_type_updated_v1_response_body = cls(
            action=action,
            actor=actor,
            context=context,
            occurred_at=occurred_at,
            targets=targets,
            version=version,
        )

        audit_logs_incident_type_updated_v1_response_body.additional_properties = d
        return audit_logs_incident_type_updated_v1_response_body

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
