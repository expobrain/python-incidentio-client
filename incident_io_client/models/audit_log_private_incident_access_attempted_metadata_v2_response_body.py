from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.audit_log_private_incident_access_attempted_metadata_v2_response_body_outcome import (
    AuditLogPrivateIncidentAccessAttemptedMetadataV2ResponseBodyOutcome,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogPrivateIncidentAccessAttemptedMetadataV2ResponseBody")


@_attrs_define
class AuditLogPrivateIncidentAccessAttemptedMetadataV2ResponseBody:
    """
    Example:
        {'outcome': 'granted'}

    Attributes:
        outcome (Union[Unset, AuditLogPrivateIncidentAccessAttemptedMetadataV2ResponseBodyOutcome]): Whether or not the
            user was able to access the private incident Example: granted.
    """

    outcome: Union[
        Unset, AuditLogPrivateIncidentAccessAttemptedMetadataV2ResponseBodyOutcome
    ] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        outcome: Union[Unset, str] = UNSET
        if not isinstance(self.outcome, Unset):
            outcome = self.outcome.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outcome is not UNSET:
            field_dict["outcome"] = outcome

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _outcome = d.pop("outcome", UNSET)
        outcome: Union[Unset, AuditLogPrivateIncidentAccessAttemptedMetadataV2ResponseBodyOutcome]
        if isinstance(_outcome, Unset):
            outcome = UNSET
        else:
            outcome = AuditLogPrivateIncidentAccessAttemptedMetadataV2ResponseBodyOutcome(_outcome)

        audit_log_private_incident_access_attempted_metadata_v2_response_body = cls(
            outcome=outcome,
        )

        audit_log_private_incident_access_attempted_metadata_v2_response_body.additional_properties = (
            d
        )
        return audit_log_private_incident_access_attempted_metadata_v2_response_body

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
