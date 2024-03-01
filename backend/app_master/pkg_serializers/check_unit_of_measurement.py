# ========================================================================
from app_master.pkg_models.check_unit_of_measurement import UOM
from utility.abstract_serializer import Serializer


# ========================================================================
class Uom(Serializer):
    class Meta:
        model = UOM
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["unit"] = f"master/unit/{instance.unit.id}"
        except Exception:
            pass
        return data
