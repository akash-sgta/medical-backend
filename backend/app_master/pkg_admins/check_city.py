# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_city import CITY


# ========================================================================
class City(Change_Log):
    """
    Customizes the Django admin interface for managing cities.

    Attributes:
        state (ForeignKey): The state to which the city belongs.
        eng_name (CharField): The English name of the city.
        local_name (CharField): The local name of the city.
    """

    # Display settings for the admin interface
    list_display = (
        "state",
        "eng_name",
        "local_name",
    ) + Change_Log.list_display
    search_fields = (
        "eng_name__icontains",
        "local_name__icontains",
    )
    list_filter = (
        "state__eng_name",
        "state__country__eng_name",
    )

    def created(self, obj):
        """
        Method to handle the creation event for City objects in the admin interface.

        Args:
            obj: The object representing the city.

        Returns:
            str: The creation details.
        """
        return super().created(CITY.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for City objects in the admin interface.

        Args:
            obj: The object representing the city.

        Returns:
            str: The change details.
        """
        return super().changed(CITY.objects.get(id=obj.id))
