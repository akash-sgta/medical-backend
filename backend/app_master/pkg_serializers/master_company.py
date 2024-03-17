# ========================================================================
from app_master.pkg_models.master_company import COMPANY
from utility.abstract_serializer import Serializer


# ========================================================================
class Company(Serializer):
    class Meta:
        model = COMPANY
        fields = "__all__"
        extra_kwargs = Serializer().extra()
