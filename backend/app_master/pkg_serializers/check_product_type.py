# ========================================================================
from app_master.pkg_models.check_product_type import PRODUCT_TYPE, PRODUCT_TYPE_T
from utility.abstract_serializer import Serializer


# ========================================================================
class Product_Type(Serializer):
    class Meta:
        model = PRODUCT_TYPE
        fields = "__all__"
        extra_kwargs = Serializer().extra()


class Product_Type_T(Serializer):
    class Meta:
        model = PRODUCT_TYPE_T
        fields = "__all__"
        extra_kwargs = Serializer().extra()
