# ========================================================================
from app_master.pkg_models.check_country import COUNTRY
from utility.abstract_serializer import Serializer


# ========================================================================
class Country(Serializer):
    class Meta:
        model = COUNTRY
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def get_continent_name(self, result):
        try:
            text = result.continent.eng_name
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
