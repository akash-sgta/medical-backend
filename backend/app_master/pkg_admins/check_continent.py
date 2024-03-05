# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_continent import CONTINENT


# ========================================================================
class Continent(Change_Log):
    """
    Customizes the Django admin interface for managing continents.

    Attributes:
        eng_name (CharField): The English name of the continent.
        local_name (CharField): The local name of the continent.
    """

    list_display = (
        "eng_name",
        "local_name",
    ) + Change_Log.list_display
    search_fields = (
        "eng_name__icontains",
        "local_name__icontains",
    )

    def created(self, obj):
        """
        Returns the creation log of the given object.

        Args:
            obj: The object for which to retrieve the creation log.

        Returns:
            str: The creation log message.
        """
        return super().created(CONTINENT.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Returns the change log of the given object.

        Args:
            obj: The object for which to retrieve the change log.

        Returns:
            str: The change log message.
        """
        return super().changed(CONTINENT.objects.get(id=obj.id))
