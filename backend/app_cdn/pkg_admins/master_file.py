# ========================================================================
from utility.abstract_admin import Change_Log
from app_cdn.pkg_models.master_file import FILE


# ========================================================================
class File(Change_Log):
    """
    Customizes the Django admin interface for managing file

    Attributes:
        id (BigAutoField): The primary key of the file.
        file_type (ForeignKey to File_Type): The type of the file.
        name (CharField): The name of the file.
    """

    list_display = (
        "id",
        "file_type",
        "name",
    ) + Change_Log.list_display
    search_fields = ("name__icontains",)
    list_filter = Change_Log.list_filter + ("type__name",)

    def file_type(self, obj):
        """
        Method to display the type of the file.
        """
        return "{}".format(obj.type.name)

    def created(self, obj):
        """
        Method to display creation details of the file in the admin interface.
        """
        return super().created(FILE.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to display change details of the file in the admin interface.
        """
        return super().changed(FILE.objects.get(id=obj.id))
