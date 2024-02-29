# ========================================================================
from app_master.pkg_models.check_city import CITY
from utility.abstract_serializer import Serializer


# ========================================================================
class City(Serializer):
    class Meta:
        model = CITY
        fields = "__all__"
        extra_kwargs = Serializer().extra()
