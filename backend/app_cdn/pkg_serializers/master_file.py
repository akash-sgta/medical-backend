# ========================================================================
from app_cdn.pkg_models.master_file import FILE
from utility.abstract_serializer import Serializer


# ========================================================================
class File(Serializer):
    class Meta:
        model = FILE
        fields = "__all__"
        extra_kwargs = Serializer().extra()
