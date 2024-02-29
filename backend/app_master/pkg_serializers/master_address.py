# ========================================================================
from app_master.pkg_models.master_address import ADDRESS
from utility.abstract_serializer import Serializer


# ========================================================================
class Address(Serializer):
    class Meta:
        model = ADDRESS
        fields = "__all__"
        extra_kwargs = Serializer().extra()
