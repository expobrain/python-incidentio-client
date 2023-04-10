from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_log_api_key_metadata_v2_response_body import (
        AuditLogAPIKeyMetadataV2ResponseBody,
    )
    from ..models.audit_log_external_resource_metadata_v2_response_body import (
        AuditLogExternalResourceMetadataV2ResponseBody,
    )
    from ..models.audit_log_user_metadata_v2_response_body import (
        AuditLogUserMetadataV2ResponseBody,
    )


T = TypeVar("T", bound="AuditLogActorMetadataV2ResponseBody")


@attr.s(auto_attribs=True)
class AuditLogActorMetadataV2ResponseBody:
    """
    Example:
        {'api_key': {'api_key_roles': ['incident_creator']}, 'external_resource': {'external_id': 'q1234',
            'resource_type': 'pager_duty_incident'}, 'user': {'base_role_slug': 'admin', 'custom_role_slugs':
            ['engineering']}}

    Attributes:
        api_key (Union[Unset, AuditLogAPIKeyMetadataV2ResponseBody]):  Example: {'api_key_roles': ['incident_creator']}.
        external_resource (Union[Unset, AuditLogExternalResourceMetadataV2ResponseBody]):  Example: {'external_id':
            'q1234', 'resource_type': 'pager_duty_incident'}.
        user (Union[Unset, AuditLogUserMetadataV2ResponseBody]):  Example: {'base_role_slug': 'admin',
            'custom_role_slugs': ['engineering']}.
    """

    api_key: Union[Unset, "AuditLogAPIKeyMetadataV2ResponseBody"] = UNSET
    external_resource: Union[Unset, "AuditLogExternalResourceMetadataV2ResponseBody"] = UNSET
    user: Union[Unset, "AuditLogUserMetadataV2ResponseBody"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        api_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api_key, Unset):
            api_key = self.api_key.to_dict()

        external_resource: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.external_resource, Unset):
            external_resource = self.external_resource.to_dict()

        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if external_resource is not UNSET:
            field_dict["external_resource"] = external_resource
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.audit_log_api_key_metadata_v2_response_body import (
            AuditLogAPIKeyMetadataV2ResponseBody,
        )
        from ..models.audit_log_external_resource_metadata_v2_response_body import (
            AuditLogExternalResourceMetadataV2ResponseBody,
        )
        from ..models.audit_log_user_metadata_v2_response_body import (
            AuditLogUserMetadataV2ResponseBody,
        )

        d = src_dict.copy()
        _api_key = d.pop("api_key", UNSET)
        api_key: Union[Unset, AuditLogAPIKeyMetadataV2ResponseBody]
        if isinstance(_api_key, Unset):
            api_key = UNSET
        else:
            api_key = AuditLogAPIKeyMetadataV2ResponseBody.from_dict(_api_key)

        _external_resource = d.pop("external_resource", UNSET)
        external_resource: Union[Unset, AuditLogExternalResourceMetadataV2ResponseBody]
        if isinstance(_external_resource, Unset):
            external_resource = UNSET
        else:
            external_resource = AuditLogExternalResourceMetadataV2ResponseBody.from_dict(
                _external_resource
            )

        _user = d.pop("user", UNSET)
        user: Union[Unset, AuditLogUserMetadataV2ResponseBody]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = AuditLogUserMetadataV2ResponseBody.from_dict(_user)

        audit_log_actor_metadata_v2_response_body = cls(
            api_key=api_key,
            external_resource=external_resource,
            user=user,
        )

        audit_log_actor_metadata_v2_response_body.additional_properties = d
        return audit_log_actor_metadata_v2_response_body

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
