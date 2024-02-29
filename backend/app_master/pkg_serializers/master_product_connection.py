# ========================================================================
from app_master.pkg_models.master_product_connection import PRODUCT_CONNECTION
from utility.abstract_serializer import Serializer


# ========================================================================
class Product_Connection(Serializer):
    class Meta:
        model = PRODUCT_CONNECTION
        fields = "__all__"
        extra_kwargs = Serializer().extra()
