# ========================================================================
from utility.abstract_admin import Change_Log
from app_cdn.pkg_models.check_file_type import FILE_TYPE


# ========================================================================
class File_Type(Change_Log):
    """
    Customizes the Django admin interface for managing file types.

    Attributes:
        name (CharField): The name of the file type.
    """

    # Display settings for the admin interface
    list_display = ("name",) + Change_Log.list_display
    search_fields = ("name__icontains",)

    def created(self, obj):
        """
        Method to display creation details of the file type in the admin interface.

        Args:
            obj: The object representing the file type.

        Returns:
            str: The creation details.
        """
        return super().created(FILE_TYPE.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to display change details of the file type in the admin interface.

        Args:
            obj: The object representing the file type.

        Returns:
            str: The change details.
        """
        return super().changed(FILE_TYPE.objects.get(id=obj.id))
