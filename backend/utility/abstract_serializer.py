# ========================================================================
from rest_framework import serializers
from rest_framework.fields import Field

from utility.methods import get_date_time_from_ts, post_error_to_terminal


# ========================================================================
class Serializer(serializers.ModelSerializer):
    def extra(self) -> dict:
        extra_kwargs = {
            "id": {"read_only": True},
            "created_on": {"read_only": True},
            "changed_on": {"read_only": True},
            "created_by": {"read_only": True},
            "changed_by": {"read_only": True},
            "company_code": {"write_only": True},  # Adjusted in views
            "is_deleted": {"write_only": True},  # Adjusted in models
        }
        return extra_kwargs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            data["created_on"] = self.get_created_on(instance)
        except Exception:
            pass
        try:
            data["changed_on"] = self.get_changed_on(instance)
        except Exception:
            pass
        return data

    def get_created_on(self, result):
        try:
            date, time = get_date_time_from_ts(result.created_on)
            text = "{} {}".format(date, time)
        except Exception as e:
            post_error_to_terminal(str(e))
            text = None
        return text

    def get_changed_on(self, result):
        if result.changed_on == 0:
            text = None
        else:
            try:
                date, time = get_date_time_from_ts(result.changed_on)
                text = "{} {}".format(date, time)
            except Exception as e:
                post_error_to_terminal(str(e))
                text = None
        return text
