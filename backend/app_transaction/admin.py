# ========================================================================
from django.contrib import admin

from app_transaction.pkg_models.inventory_management.product_inventory import (
    PRODUCT_INVENTORY_SUMMARY,
    PRODUCT_INVENTORY_ITEM,
)
from app_transaction.pkg_models.sales_and_distribution.product_sales import (
    PRODUCT_SALES_SUMMARY,
    PRODUCT_SALES_ITEM,
    PRODUCT_SALES_REFERRAL,
)

from app_transaction.pkg_admins.inventory_management.product_inventory import (
    Product_Inventory_Summary,
    Product_Inventory_Item,
)
from app_transaction.pkg_admins.sales_and_distribution.product_sales import (
    Product_Sales_Summary,
    Product_Sales_Item,
    Product_Sales_Referral,
)

# ========================================================================

admin.site.register(PRODUCT_SALES_SUMMARY, Product_Sales_Summary)
admin.site.register(PRODUCT_SALES_ITEM, Product_Sales_Item)
admin.site.register(PRODUCT_SALES_REFERRAL, Product_Sales_Referral)
admin.site.register(PRODUCT_INVENTORY_SUMMARY, Product_Inventory_Summary)
admin.site.register(PRODUCT_INVENTORY_ITEM, Product_Inventory_Item)
