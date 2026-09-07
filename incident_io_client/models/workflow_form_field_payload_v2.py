from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowFormFieldPayloadV2")


@_attrs_define
class WorkflowFormFieldPayloadV2:
    """
    Example:
        {'array': True, 'description': 'The customer affected by this incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'key': 'affected_customer', 'required': True, 'title': 'Affected customer', 'type': 'User'}

    Attributes:
        key (str): The key used to reference this field in the workflow scope Example: affected_customer.
        title (str): Human readable title shown in the form Example: Affected customer.
        type (str): The engine resource type of this field Example: User.
        array (Union[Unset, bool]): Whether this field holds a list of values rather than a single value Example: True.
        description (Union[Unset, str]): Optional help text shown beneath the field Example: The customer affected by
            this incident.
        id (Union[Unset, str]): Stable identifier for this field; omit to create a new field Example:
            01FCNDV6P870EA6S7TK1DSYDG0.
        required (Union[Unset, bool]): Whether this field must be filled in when running the workflow Example: True.
    """

    key: str
    title: str
    type: str
    array: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        title = self.title

        type = self.type

        array = self.array

        description = self.description

        id = self.id

        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "title": title,
                "type": type,
            }
        )
        if array is not UNSET:
            field_dict["array"] = array
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        title = d.pop("title")

        type = d.pop("type")

        array = d.pop("array", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        required = d.pop("required", UNSET)

        workflow_form_field_payload_v2 = cls(
            key=key,
            title=title,
            type=type,
            array=array,
            description=description,
            id=id,
            required=required,
        )

        workflow_form_field_payload_v2.additional_properties = d
        return workflow_form_field_payload_v2

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
