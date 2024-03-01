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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["type"] = f"/master/product_type/{instance.type.id}"
        except Exception:
            pass
        try:
            data["lang"] = f"/master/language/{instance.lang.id}"
        except Exception:
            pass
        try:
            data["text"] = f"/master/text/{instance.text.id}"
        except Exception:
            pass
        return data
