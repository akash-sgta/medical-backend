# ========================================================================
from app_master.pkg_models.check_city import CITY
from utility.abstract_serializer import Serializer


# ========================================================================
class City(Serializer):
    class Meta:
        model = CITY
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def get_state_name(self, result):
        try:
            text = result.state.eng_name
        except Exception as e:
            text = None
        return text

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["state"] = self.get_state_name(instance)
        except Exception:
            pass
        return data
