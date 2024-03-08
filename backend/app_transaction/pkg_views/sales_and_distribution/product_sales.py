# ========================================================================
from utility.abstract_admin import Change_Log
from app_transaction.pkg_models.sales_and_distribution.product_sales import (
    PRODUCT_SALES_SUMMARY,
    PRODUCT_SALES_ITEM,
    PRODUCT_SALES_REFERRAL,
)


# ========================================================================
class Product_Sales_Summary(Change_Log):
    list_display = (
        "buyer",
        "id",
    ) + Change_Log.list_display
    search_fields = ("buyer__email__icontains",)
    list_filter = ("buyer__email",)
    ordering = (
        "buyer",
        "-id",
    )

    def created(self, obj):
        return super().created(PRODUCT_SALES_SUMMARY.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_SALES_SUMMARY.objects.get(id=obj.id))


class Product_Sales_Item(Change_Log):
    list_display = (
        "summary",
        "product",
        "id",
    ) + Change_Log.list_display
    search_fields = (
        "summary__buyer__email__icontains",
        "product__eng_name",
    )
    list_filter = ("summary__buyer__email",)
    ordering = (
        "summary",
        "product",
        "-id",
    )

    def created(self, obj):
        return super().created(PRODUCT_SALES_ITEM.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_SALES_ITEM.objects.get(id=obj.id))


class Product_Sales_Referral(Change_Log):
    list_display = (
        "referral",
        "summary",
        "id",
    ) + Change_Log.list_display
    search_fields = ("referral__email__icontains",)
    list_filter = ("referral__email",)
    ordering = (
        "referral",
        "summary",
        "-id",
    )

    def created(self, obj):
        return super().created(PRODUCT_SALES_REFERRAL.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT_SALES_REFERRAL.objects.get(id=obj.id))
