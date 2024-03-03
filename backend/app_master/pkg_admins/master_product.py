# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_product import PRODUCT


# ========================================================================
class Product(Change_Log):
    """
    Customizes the Django admin interface for managing products.

    Attributes:
        name (CharField): The name of the product.
        price (DecimalField): The price of the product.
        currency (ForeignKey): The currency used for the product price.
        rx (BooleanField): Indicates whether a prescription is required for the product.
    """

    # Display settings for the admin interface
    list_display = (
        "id",
        "name",
        "price",
        "currency",
        "rx",
    ) + Change_Log.list_display
    search_fields = ("name__icontains",)
    list_filter = ("type",) + Change_Log.list_filter

    def rx(self, obj):
        """
        Method to display whether a prescription is required for the product.

        Args:
            obj: The object representing the product.

        Returns:
            bool: True if a prescription is required, False otherwise.
        """
        return obj.is_prescription_required

    def created(self, obj):
        """
        Method to handle the creation event for Product objects in the admin interface.

        Args:
            obj: The object representing the product.

        Returns:
            str: The creation details.
        """
        return super().created(PRODUCT.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Product objects in the admin interface.

        Args:
            obj: The object representing the product.

        Returns:
            str: The change details.
        """
        return super().changed(PRODUCT.objects.get(id=obj.id))
