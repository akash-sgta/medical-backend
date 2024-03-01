# ========================================================================
from app_master.pkg_models.master_text import TEXT
from utility.abstract_serializer import Serializer


# ========================================================================
class Text(Serializer):
    class Meta:
        model = TEXT
        fields = "__all__"
        extra_kwargs = Serializer().extra()
