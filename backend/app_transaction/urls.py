# ========================================================================
from django.urls import re_path

from app_transaction.pkg_views.inventory_management.product_inventory import (
    Product_Inventory_Summary,
    Product_Inventory_Item,
)
from app_transaction.pkg_views.sales_and_distribution.product_sales import (
    Product_Sales_Summary,
    Product_Sales_Item,
    Product_Sales_Referral,
)

# ========================================================================

urlpatterns = [
    re_path(
        r"transaction/inventory_management/product_inventory/summary/(?P<pk>\d*)$",
        Product_Inventory_Summary.as_view(),
        name="Transaction_Product_Inventory_Summary",
    ),
    re_path(
        r"transaction/inventory_management/product_inventory/item/(?P<pk>\d*)$",
        Product_Inventory_Item.as_view(),
        name="Transaction_Product_Inventory_Item",
    ),
    re_path(
        r"transaction/sales_and_distribution/product_sales/summary/(?P<pk>\d*)$",
        Product_Sales_Summary.as_view(),
        name="Transaction_Product_Sales_Summary",
    ),
    re_path(
        r"transaction/sales_and_distribution/product_sales/item/(?P<pk>\d*)$",
        Product_Sales_Item.as_view(),
        name="Transaction_Product_Sales_Item",
    ),
    re_path(
        r"transaction/sales_and_distribution/product_sales/referral/(?P<pk>\d*)$",
        Product_Sales_Referral.as_view(),
        name="Transaction_Product_Sales_Referral",
    ),
]
