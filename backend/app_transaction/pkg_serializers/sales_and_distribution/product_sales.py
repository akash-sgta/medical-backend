# ========================================================================
from app_transaction.pkg_models.sales_and_distribution.product_sales import (
    PRODUCT_SALES_SUMMARY,
    PRODUCT_SALES_ITEM,
    PRODUCT_SALES_REFERRAL,
)
from utility.abstract_serializer import Serializer


# ========================================================================
class Product_Sales_Summary(Serializer):
    class Meta:
        model = PRODUCT_SALES_SUMMARY
        fields = "__all__"
        extra_kwargs = Serializer().extra()


class Product_Sales_Item(Serializer):
    class Meta:
        model = PRODUCT_SALES_ITEM
        fields = "__all__"
        extra_kwargs = Serializer().extra()


class Product_Sales_Referral(Serializer):
    class Meta:
        model = PRODUCT_SALES_REFERRAL
        fields = "__all__"
        extra_kwargs = Serializer().extra()
