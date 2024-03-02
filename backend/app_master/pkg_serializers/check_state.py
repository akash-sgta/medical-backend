# ========================================================================
from app_master.pkg_models.check_state import STATE
from utility.abstract_serializer import Serializer


# ========================================================================
class State(Serializer):
    class Meta:
        model = STATE
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["country"] = f"master/check/country/{instance.country.id}"
        except Exception:
            pass
        return data
