# ========================================================================
from app_master.pkg_models.master_product import PRODUCT
from utility.abstract_serializer import Serializer


# ========================================================================
class Product(Serializer):
    class Meta:
        model = PRODUCT
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["type"] = f"master/check/type/{instance.type.id}"
        except Exception:
            pass
        try:
            data["image_01"] = f"cdn/master/file/{instance.image_01.id}"
        except Exception:
            pass
        try:
            data["image_02"] = f"cdn/master/file/{instance.image_02.id}"
        except Exception:
            pass
        try:
            data["image_03"] = f"cdn/master/file/{instance.image_03.id}"
        except Exception:
            pass
        try:
            data["currency"] = f"master/check/currency/{instance.currency.id}"
        except Exception:
            pass
        try:
            data["description"] = f"master/master/text/{instance.description.id}"
        except Exception:
            pass
        try:
            data[
                "storage_instructions"
            ] = f"master/master/text/{instance.storage_instructions.id}"
        except Exception:
            pass
        try:
            data["side_effects"] = f"master/master/text/{instance.side_effects.id}"
        except Exception:
            pass
        try:
            data[
                "warnings_precautions"
            ] = f"master/master/text/{instance.warnings_precautions.id}"
        except Exception:
            pass
        return data
