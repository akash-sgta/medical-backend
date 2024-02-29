# ========================================================================
from app_master.pkg_models.master_text import TEXT
from utility.abstract_serializer import Serializer


# ========================================================================
class Text(Serializer):
    class Meta:
        model = TEXT
        fields = "__all__"
        extra_kwargs = Serializer().extra()

    def get_lang_id(self, result):
        try:
            text = result.lang.eng_name
        except Exception as e:
            text = None
        return text

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["lang"] = self.get_lang_id(instance)
        except Exception:
            pass
        return data
