# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_unit import UNIT


# ========================================================================
class Unit(Change_Log):
    """
    Customizes the Django admin interface for managing units.

    Attributes:
        name (CharField): The name of the unit.
    """

    # Display settings for the admin interface
    list_display = ("name",) + Change_Log.list_display
    search_fields = ("name__icontains",)

    def created(self, obj):
        """
        Method to handle the creation event for Unit objects in the admin interface.

        Args:
            obj: The object representing the unit.

        Returns:
            str: The creation details.
        """
        return super().created(UNIT.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Unit objects in the admin interface.

        Args:
            obj: The object representing the unit.

        Returns:
            str: The change details.
        """
        return super().changed(UNIT.objects.get(id=obj.id))
