# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_address import ADDRESS


# ========================================================================
class Address(Change_Log):
    list_display = (
        "id",
        "country_name",
        "state_name",
        "city_name",
        "postal_code",
        "latitude",
        "longitude",
    ) + super().list_display
    search_fields = ("id__icontains",)
    list_filter = (
        "city__state__country__eng_name",
        "city__state__eng_name",
        "city__eng_name",
    ) + super().list_filter

    def country_name(self, obj):
        return "{}".format(obj.city.state.country.eng_name)

    def state_name(self, obj):
        return "{}".format(obj.city.state.eng_name)

    def city_name(self, obj):
        return "{}".format(obj.city.eng_name)

    def created(self, obj):
        return super().created(ADDRESS.objects.get(id=obj.id))

    def changed(self, obj):
        return super().changed(ADDRESS.objects.get(id=obj.id))
