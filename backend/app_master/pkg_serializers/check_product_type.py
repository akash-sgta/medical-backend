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

    def get_type_name(self, result):
        try:
            text = result.type.name
        except Exception as e:
            text = None
        return text

    def get_text_data(self, result):
        try:
            text = result.type.name
        except Exception as e:
            text = None
        return text

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["continent"] = self.get_continent_name(instance)
        except Exception:
            pass
        return data
