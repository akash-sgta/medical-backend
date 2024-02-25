# ========================================================================
from app_master.pkg_models.check_language import LANGUAGE
from utility.abstract_serializer import Serializer


# ========================================================================
class Language(Serializer):
    class Meta:
        model = LANGUAGE
        fields = "__all__"
        extra_kwargs = Serializer().extra()
