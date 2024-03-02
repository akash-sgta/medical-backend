# ========================================================================
from app_master.pkg_models.master_address import ADDRESS
from utility.abstract_serializer import Serializer


# ========================================================================
class Address(Serializer):
    class Meta:
        model = ADDRESS
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["city"] = f"master/check/city/{instance.city.id}"
        except Exception:
            pass
        try:
            data[
                "additional_line"
            ] = f"master/master/text/{instance.additional_line.id}"
        except Exception:
            pass
        return data
