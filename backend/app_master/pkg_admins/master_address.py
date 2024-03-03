# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_address import ADDRESS


# ========================================================================
class Address(Change_Log):
    """
    Customizes the Django admin interface for managing addresses.

    Attributes:
        id (BigAutoField): The primary key of the address.
        country_name (str): The name of the country.
        state_name (str): The name of the state.
        city_name (str): The name of the city.
        postal_code (str): The postal code of the address.
        latitude (DecimalField): The latitude coordinate of the address.
        longitude (DecimalField): The longitude coordinate of the address.
    """

    # Display settings for the admin interface
    list_display = (
        "id",
        "country_name",
        "state_name",
        "city_name",
        "postal_code",
        "latitude",
        "longitude",
    ) + Change_Log.list_display
    search_fields = ("id__icontains",)
    list_filter = (
        "city__state__country__eng_name",
        "city__state__eng_name",
        "city__eng_name",
    ) + Change_Log.list_filter

    def country_name(self, obj):
        """
        Method to display the name of the country associated with the address.

        Args:
            obj: The object representing the address.

        Returns:
            str: The name of the country.
        """
        return "{}".format(obj.city.state.country.eng_name)

    def state_name(self, obj):
        """
        Method to display the name of the state associated with the address.

        Args:
            obj: The object representing the address.

        Returns:
            str: The name of the state.
        """
        return "{}".format(obj.city.state.eng_name)

    def city_name(self, obj):
        """
        Method to display the name of the city associated with the address.

        Args:
            obj: The object representing the address.

        Returns:
            str: The name of the city.
        """
        return "{}".format(obj.city.eng_name)

    def created(self, obj):
        """
        Method to handle the creation event for Address objects in the admin interface.

        Args:
            obj: The object representing the address.

        Returns:
            str: The creation details.
        """
        return super().created(ADDRESS.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Address objects in the admin interface.

        Args:
            obj: The object representing the address.

        Returns:
            str: The change details.
        """
        return super().changed(ADDRESS.objects.get(id=obj.id))
