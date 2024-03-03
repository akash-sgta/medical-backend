# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_credential import CREDENTIAL


# ========================================================================
class Credential(Change_Log):
    """
    Customizes the Django admin interface for managing credentials.

    Attributes:
        email (EmailField): The email associated with the credential.
        is_admin (BooleanField): Indicates whether the credential has admin privileges.
        is_internal_user (BooleanField): Indicates whether the credential represents an internal user.
        is_external_user (BooleanField): Indicates whether the credential represents an external user.
    """

    # Display settings for the admin interface
    list_display = (
        "email",
        "is_admin",
        "is_internal_user",
        "is_external_user",
    ) + Change_Log.list_display
    search_fields = ("email__icontains",)
    list_filter = (
        "is_admin",
        "is_internal_user",
        "is_external_user",
    ) + Change_Log.list_filter

    def created(self, obj):
        """
        Method to handle the creation event for Credential objects in the admin interface.

        Args:
            obj: The object representing the credential.

        Returns:
            str: The creation details.
        """
        return super().created(CREDENTIAL.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Credential objects in the admin interface.

        Args:
            obj: The object representing the credential.

        Returns:
            str: The change details.
        """
        return super().changed(CREDENTIAL.objects.get(id=obj.id))
