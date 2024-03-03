# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_text import TEXT


# ========================================================================
class Text(Change_Log):
    """
    Customizes the Django admin interface for managing text.

    Attributes:
        lang_name (CharField): The combined name of the language.
    """

    # Display settings for the admin interface
    list_display = (
        "id",
        "lang_name",
    ) + Change_Log.list_display
    search_fields = ("id__icontains",)

    def lang_name(self, obj):
        """
        Method to display the combined name of the language.

        Args:
            obj: The object representing the text.

        Returns:
            str: The combined name of the language.
        """
        return "{}_{}".format(obj.lang.eng_name, obj.lang.local_name)

    def created(self, obj):
        """
        Method to handle the creation event for Text objects in the admin interface.

        Args:
            obj: The object representing the text.

        Returns:
            str: The creation details.
        """
        return super().created(TEXT.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Text objects in the admin interface.

        Args:
            obj: The object representing the text.

        Returns:
            str: The change details.
        """
        return super().changed(TEXT.objects.get(id=obj.id))
