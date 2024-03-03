# ========================================================================
from utility.abstract_admin import Change_Log
from app_cdn.pkg_models.master_file import FILE


# ========================================================================
class File(Change_Log):
    """
    Customizes the Django admin interface for managing files.

    Attributes:
        file_type (ForeignKey to File_Type): The type of the file.
        name (CharField): The name of the file.
    """

    # Display settings for the admin interface
    list_display = (
        "file_type",
        "name",
    ) + Change_Log.list_display
    search_fields = ("name__icontains",)
    list_filter = Change_Log.list_filter + ("type__name",)

    def file_type(self, obj):
        """
        Method to display the type of the file.

        Args:
            obj: The object representing the file.

        Returns:
            str: The type of the file.
        """
        return "{}".format(obj.type.name)

    def created(self, obj):
        """
        Method to display creation details of the file in the admin interface.

        Args:
            obj: The object representing the file.

        Returns:
            str: The creation details.
        """
        return super().created(FILE.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to display change details of the file in the admin interface.

        Args:
            obj: The object representing the file.

        Returns:
            str: The change details.
        """
        return super().changed(FILE.objects.get(id=obj.id))
