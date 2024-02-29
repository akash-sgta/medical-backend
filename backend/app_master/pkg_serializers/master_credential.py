# ========================================================================
from app_master.pkg_models.master_credential import CREDENTIAL
from utility.abstract_serializer import Serializer


# ========================================================================
class Credential(Serializer):
    class Meta:
        model = CREDENTIAL
        fields = "__all__"
        extra_kwargs = Serializer().extra()
