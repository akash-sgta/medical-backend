# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_state import STATE


# ========================================================================
class State(Change_Log):
    """
    Customizes the Django admin interface for managing states.

    Attributes:
        country_name (CharField): The name of the country to which the state belongs.
        eng_name (CharField): The English name of the state.
    """

    # Display settings for the admin interface
    list_display = (
        "country_name",
        "eng_name",
    ) + Change_Log.list_display
    search_fields = (
        "country__eng_name__icontains",
        "eng_name__icontains",
    )
    list_filter = ("country__eng_name",) + Change_Log.list_filter

    def country_name(self, obj):
        """
        Method to display the name of the country to which the state belongs.

        Args:
            obj: The object representing the state.

        Returns:
            str: The name of the country.
        """
        return obj.country.eng_name

    def created(self, obj):
        """
        Method to handle the creation event for State objects in the admin interface.

        Args:
            obj: The object representing the state.

        Returns:
            str: The creation details.
        """
        return super().created(STATE.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for State objects in the admin interface.

        Args:
            obj: The object representing the state.

        Returns:
            str: The change details.
        """
        return super().changed(STATE.objects.get(id=obj.id))
