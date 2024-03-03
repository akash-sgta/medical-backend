# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_unit_of_measurement import UOM


# ========================================================================
class Uom(Change_Log):
    """
    Customizes the Django admin interface for managing units of measurement.

    Attributes:
        unit (ForeignKey): The unit associated with the unit of measurement.
        name (CharField): The name of the unit of measurement.
    """

    # Display settings for the admin interface
    list_display = (
        "unit_name",
        "name",
    ) + Change_Log.list_display
    search_fields = (
        "unit__name__icontains",
        "name__icontains",
    )
    list_filter = ("unit__name",) + Change_Log.list_filter

    def unit_name(self, obj):
        """
        Method to display the name of the unit associated with the unit of measurement.

        Args:
            obj: The object representing the unit of measurement.

        Returns:
            str: The name of the associated unit.
        """
        return obj.unit.name

    def created(self, obj):
        """
        Method to handle the creation event for Unit of Measurement objects in the admin interface.

        Args:
            obj: The object representing the unit of measurement.

        Returns:
            str: The creation details.
        """
        return super().created(UOM.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Unit of Measurement objects in the admin interface.

        Args:
            obj: The object representing the unit of measurement.

        Returns:
            str: The change details.
        """
        return super().changed(UOM.objects.get(id=obj.id))
