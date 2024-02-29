# ========================================================================
from app_master.pkg_models.master_product import PRODUCT
from utility.abstract_serializer import Serializer


# ========================================================================
class Product(Serializer):
    class Meta:
        model = PRODUCT
        fields = "__all__"
        extra_kwargs = Serializer().extra()
