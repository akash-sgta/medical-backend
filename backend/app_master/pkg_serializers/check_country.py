# ========================================================================
from app_master.pkg_models.check_country import COUNTRY
from utility.abstract_serializer import Serializer


# ========================================================================
class Country(Serializer):
    class Meta:
        model = COUNTRY
        fields = "__all__"
        extra_kwargs = Serializer().extra()
