# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_product import PRODUCT


# ========================================================================
class Product(Change_Log):
    list_display = (
        "id",
        "name",
        "price",
        "currency",
        "rx",
    ) + super().list_display
    search_fields = ("email__icontains",)
    list_filter = ("type",) + super().list_filter

    def rx(self, obj):
        return obj.is_prescription_required

    def created(self, obj):
        return super().created(PRODUCT.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(PRODUCT.objects.get(id=obj.id))
