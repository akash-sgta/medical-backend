# ========================================================================
from app_cdn.pkg_models.check_file_type import FILE_TYPE
from utility.abstract_serializer import Serializer


# ========================================================================
class File_Type(Serializer):
    class Meta:
        model = FILE_TYPE
        fields = "__all__"
        extra_kwargs = Serializer().extra()
