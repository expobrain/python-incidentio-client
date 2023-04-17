from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_entry_reference_v2_response_body import (
        CatalogEntryReferenceV2ResponseBody,
    )


T = TypeVar("T", bound="CatalogAttributeValueV2ResponseBody")


@attr.s(auto_attribs=True)
class CatalogAttributeValueV2ResponseBody:
    """
    Example:
        {'catalog_entry': {'catalog_entry_id': '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id':
            '01FCNDV6P870EA6S7TK1DSYDG0'}, 'image_url': 'https://avatars.slack-
            edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg', 'is_image_slack_icon': False, 'label':
            'Lawrence Jones', 'literal': 'SEV123', 'sort_key': '000020'}

    Attributes:
        label (str): Human readable label to be displayed for user to select Example: Lawrence Jones.
        sort_key (str): Gives an indication of how to sort the options when displayed to the user Example: 000020.
        catalog_entry (Union[Unset, CatalogEntryReferenceV2ResponseBody]):  Example: {'catalog_entry_id':
            '01FCNDV6P870EA6S7TK1DSYDG0', 'catalog_type_id': '01FCNDV6P870EA6S7TK1DSYDG0'}.
        image_url (Union[Unset, str]): If appropriate, URL to an image that can be displayed alongside the option
            Example: https://avatars.slack-edge.com/2021-08-09/2372763167857_6f65d94928b0a0ac590b_192.jpg.
        is_image_slack_icon (Union[Unset, bool]): If true, the image_url is a Slack icon and should be displayed as such
        literal (Union[Unset, str]): If set, this is the literal value of the step parameter Example: SEV123.
    """

    label: str
    sort_key: str
    catalog_entry: Union[Unset, "CatalogEntryReferenceV2ResponseBody"] = UNSET
    image_url: Union[Unset, str] = UNSET
    is_image_slack_icon: Union[Unset, bool] = UNSET
    literal: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        sort_key = self.sort_key
        catalog_entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.catalog_entry, Unset):
            catalog_entry = self.catalog_entry.to_dict()

        image_url = self.image_url
        is_image_slack_icon = self.is_image_slack_icon
        literal = self.literal

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
                "sort_key": sort_key,
            }
        )
        if catalog_entry is not UNSET:
            field_dict["catalog_entry"] = catalog_entry
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if is_image_slack_icon is not UNSET:
            field_dict["is_image_slack_icon"] = is_image_slack_icon
        if literal is not UNSET:
            field_dict["literal"] = literal

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.catalog_entry_reference_v2_response_body import (
            CatalogEntryReferenceV2ResponseBody,
        )

        d = src_dict.copy()
        label = d.pop("label")

        sort_key = d.pop("sort_key")

        _catalog_entry = d.pop("catalog_entry", UNSET)
        catalog_entry: Union[Unset, CatalogEntryReferenceV2ResponseBody]
        if isinstance(_catalog_entry, Unset):
            catalog_entry = UNSET
        else:
            catalog_entry = CatalogEntryReferenceV2ResponseBody.from_dict(_catalog_entry)

        image_url = d.pop("image_url", UNSET)

        is_image_slack_icon = d.pop("is_image_slack_icon", UNSET)

        literal = d.pop("literal", UNSET)

        catalog_attribute_value_v2_response_body = cls(
            label=label,
            sort_key=sort_key,
            catalog_entry=catalog_entry,
            image_url=image_url,
            is_image_slack_icon=is_image_slack_icon,
            literal=literal,
        )

        catalog_attribute_value_v2_response_body.additional_properties = d
        return catalog_attribute_value_v2_response_body

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
