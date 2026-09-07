from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowFormFieldV2")


@_attrs_define
class WorkflowFormFieldV2:
    """
    Example:
        {'array': True, 'description': 'The customer affected by this incident', 'id': '01FCNDV6P870EA6S7TK1DSYDG0',
            'key': 'affected_customer', 'required': True, 'title': 'Affected customer', 'type': 'User'}

    Attributes:
        array (bool): Whether this field holds a list of values rather than a single value Example: True.
        id (str): Stable identifier for this form field, preserved across versions Example: 01FCNDV6P870EA6S7TK1DSYDG0.
        key (str): The key used to reference this field in the workflow scope Example: affected_customer.
        required (bool): Whether this field must be filled in when running the workflow Example: True.
        title (str): Human readable title shown in the form Example: Affected customer.
        type (str): The engine resource type of this field Example: User.
        description (Union[Unset, str]): Optional help text shown beneath the field Example: The customer affected by
            this incident.
    """

    array: bool
    id: str
    key: str
    required: bool
    title: str
    type: str
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        array = self.array

        id = self.id

        key = self.key

        required = self.required

        title = self.title

        type = self.type

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "array": array,
                "id": id,
                "key": key,
                "required": required,
                "title": title,
                "type": type,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        array = d.pop("array")

        id = d.pop("id")

        key = d.pop("key")

        required = d.pop("required")

        title = d.pop("title")

        type = d.pop("type")

        description = d.pop("description", UNSET)

        workflow_form_field_v2 = cls(
            array=array,
            id=id,
            key=key,
            required=required,
            title=title,
            type=type,
            description=description,
        )

        workflow_form_field_v2.additional_properties = d
        return workflow_form_field_v2

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
