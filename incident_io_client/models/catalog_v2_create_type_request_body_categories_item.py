from enum import Enum


class CatalogV2CreateTypeRequestBodyCategoriesItem(str, Enum):
    CUSTOMER = "customer"
    ISSUE_TRACKER = "issue-tracker"
    ON_CALL = "on-call"
    PRODUCT_FEATURE = "product-feature"
    SERVICE = "service"
    TEAM = "team"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
