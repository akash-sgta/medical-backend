# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_language import LANGUAGE


# ========================================================================
class Language(Change_Log):
    """
    Customizes the Django admin interface for managing languages.

    Attributes:
        eng_name (CharField): The English name of the language.
        local_name (CharField): The local name of the language.
    """

    # Display settings for the admin interface
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
        Method to handle the creation event for Language objects in the admin interface.

        Args:
            obj: The object representing the language.

        Returns:
            str: The creation details.
        """
        return super().created(LANGUAGE.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Language objects in the admin interface.

        Args:
            obj: The object representing the language.

        Returns:
            str: The change details.
        """
        return super().changed(LANGUAGE.objects.get(id=obj.id))
