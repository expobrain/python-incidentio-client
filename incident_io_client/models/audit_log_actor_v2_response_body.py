from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.audit_log_actor_v2_response_body_type import (
    AuditLogActorV2ResponseBodyType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_log_actor_metadata_v2_response_body import (
        AuditLogActorMetadataV2ResponseBody,
    )


T = TypeVar("T", bound="AuditLogActorV2ResponseBody")


@attr.s(auto_attribs=True)
class AuditLogActorV2ResponseBody:
    """
    Example:
        {'id': '01FCNDV6P870EA6S7TK1DSYDG0', 'metadata': {'api_key': {'api_key_roles': ['incident_creator']},
            'external_resource': {'external_id': 'q1234', 'resource_type': 'pager_duty_incident'}, 'user':
            {'base_role_slug': 'admin', 'custom_role_slugs': ['engineering']}}, 'name': 'John Doe', 'type': 'user'}

    Attributes:
        id (str): The ID of the actor Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        type (AuditLogActorV2ResponseBodyType): The type of actor Example: user.
        metadata (Union[Unset, AuditLogActorMetadataV2ResponseBody]):  Example: {'api_key': {'api_key_roles':
            ['incident_creator']}, 'external_resource': {'external_id': 'q1234', 'resource_type': 'pager_duty_incident'},
            'user': {'base_role_slug': 'admin', 'custom_role_slugs': ['engineering']}}.
        name (Union[Unset, str]): The name of the actor Example: John Doe.
    """

    id: str
    type: AuditLogActorV2ResponseBodyType
    metadata: Union[Unset, "AuditLogActorMetadataV2ResponseBody"] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.audit_log_actor_metadata_v2_response_body import (
            AuditLogActorMetadataV2ResponseBody,
        )

        d = src_dict.copy()
        id = d.pop("id")

        type = AuditLogActorV2ResponseBodyType(d.pop("type"))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AuditLogActorMetadataV2ResponseBody]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AuditLogActorMetadataV2ResponseBody.from_dict(_metadata)

        name = d.pop("name", UNSET)

        audit_log_actor_v2_response_body = cls(
            id=id,
            type=type,
            metadata=metadata,
            name=name,
        )

        audit_log_actor_v2_response_body.additional_properties = d
        return audit_log_actor_v2_response_body

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
