# ========================================================================
from app_master.pkg_models.requirement_connection import (
    REQUIREMENT_CONNECTION,
)
from utility.abstract_serializer import Serializer


# ========================================================================
class Requirement_Connection(Serializer):
    class Meta:
        model = REQUIREMENT_CONNECTION
        fields = "__all__"
        extra_kwargs = Serializer().extra()
