# ========================================================================
from app_cdn.pkg_models.master_file import FILE
from utility.abstract_serializer import Serializer


# ========================================================================
class File(Serializer):
    class Meta:
        model = FILE
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["type"] = f"/cdn/check/file_type/{instance.type.id}"
        except Exception:
            pass
        return data
