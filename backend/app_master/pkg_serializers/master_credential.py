# ========================================================================
from app_master.pkg_models.master_credential import CREDENTIAL
from utility.abstract_serializer import Serializer


# ========================================================================
class Credential(Serializer):
    class Meta:
        model = CREDENTIAL
        fields = "__all__"
        extra_kwargs = (
            Serializer().extra()
            # .update(
            #     {
            #         "pwd": {"write_only": True},
            #     }
            # )
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["pwd"] = "▓R▓E▓D▓A▓C▓T▓E▓D▓"
        except Exception:
            pass
        return data
