# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_country import COUNTRY


# ========================================================================
class Country(Change_Log):
    """
    Customizes the Django admin interface for managing countries.

    Attributes:
        continent (ForeignKey): The continent to which the country belongs.
        eng_name (CharField): The English name of the country.
        local_name (CharField): The local name of the country.
    """

    # Display settings for the admin interface
    list_display = (
        "continent",
        "eng_name",
        "local_name",
    ) + Change_Log.list_display
    search_fields = (
        "eng_name__icontains",
        "local_name__icontains",
    )

    def created(self, obj):
        """
        Method to handle the creation event for Country objects in the admin interface.

        Args:
            obj: The object representing the country.

        Returns:
            str: The creation details.
        """
        return super().created(COUNTRY.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Country objects in the admin interface.

        Args:
            obj: The object representing the country.

        Returns:
            str: The change details.
        """
        return super().changed(COUNTRY.objects.get(id=obj.id))
