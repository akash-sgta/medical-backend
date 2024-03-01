# ========================================================================
from app_master.pkg_models.check_state import STATE
from utility.abstract_serializer import Serializer


# ========================================================================
class State(Serializer):
    class Meta:
        model = STATE
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def get_country_name(self, result):
        try:
            text = result.country.eng_name
        except Exception as e:
            text = None
        return text

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["country"] = self.get_country_name(instance)
        except Exception:
            pass
        return data
