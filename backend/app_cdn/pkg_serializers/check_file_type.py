# ========================================================================
from app_cdn.pkg_models.check_file_type import FILE_TYPE
from utility.abstract_serializer import Serializer


# ========================================================================
class File_Type(Serializer):
    """
    Serializer for File_Type model.
    """

    class Meta:
        """
        Metadata for File_Type serializer.
        """

        model = FILE_TYPE
        fields = "__all__"
        extra_kwargs = Serializer().extra()
