# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_profile import PROFILE


# ========================================================================
class Profile(Change_Log):
    """
    Customizes the Django admin interface for managing profiles.

    Attributes:
        email (CharField): The email address associated with the profile.
        first_name (CharField): The first name of the profile owner.
        middle_name (CharField): The middle name of the profile owner.
        last_name (CharField): The last name of the profile owner.
        phone_number (CharField): The phone number associated with the profile.
        address_short (CharField): A shortened version of the address associated with the profile.
    """

    # Display settings for the admin interface
    list_display = (
        "id",
        "email",
        "first_name",
        "middle_name",
        "last_name",
        "phone_number",
        "address_short",
    ) + Change_Log.list_display
    search_fields = (
        "cred__email__icontains",
        "first_name__icontains",
        "middle_name__icontains",
        "last_name__icontains",
    )

    def email(self, obj):
        """
        Method to display the email address associated with the profile.

        Args:
            obj: The object representing the profile.

        Returns:
            str: The email address.
        """
        return obj.cred.email

    def address_short(self, obj):
        """
        Method to display a shortened version of the address associated with the profile.

        Args:
            obj: The object representing the profile.

        Returns:
            str: A shortened version of the address.
        """
        return obj.address.street[:32]

    def created(self, obj):
        """
        Method to handle the creation event for Profile objects in the admin interface.

        Args:
            obj: The object representing the profile.

        Returns:
            str: The creation details.
        """
        return super().created(PROFILE.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Profile objects in the admin interface.

        Args:
            obj: The object representing the profile.

        Returns:
            str: The change details.
        """
        return super().changed(PROFILE.objects.get(id=obj.id))
