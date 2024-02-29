# ========================================================================
from django.contrib import admin
from utility.methods import get_date_time_from_ts, post_error_to_terminal


# ========================================================================


class Change_Log(admin.ModelAdmin):
    list_display = (
        "created",
        "changed",
        "company_code",
    )
    readonly_fields = (
        "created_on",
        "changed_on",
        "created_by",
        "changed_by",
    )
    list_filter = ("company_code",)

    def created(self, result):
        try:
            date, time = get_date_time_from_ts(result.created_on)
            text = "{} {}".format(date, time)
        except Exception as e:
            post_error_to_terminal(str(e))
            text = None
        return text

    def changed(self, result):
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
