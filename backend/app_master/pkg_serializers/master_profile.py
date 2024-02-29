# ========================================================================
from app_master.pkg_models.master_profile import PROFILE
from utility.abstract_serializer import Serializer


# ========================================================================
class Profile(Serializer):
    class Meta:
        model = PROFILE
        fields = "__all__"
        extra_kwargs = Serializer().extra()
