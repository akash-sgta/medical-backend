# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.master_product_connection import PRODUCT_CONNECTION


# ========================================================================
class Product_Connection(Change_Log):
    """
    Customizes the Django admin interface for managing product connections.

    Attributes:
        parent_name (CharField): The name of the parent product in the connection.
        parent_uom (CharField): The unit of measure of the parent product in the connection.
        parent_quantity (DecimalField): The quantity of the parent product in the connection.
        child_name (CharField): The name of the child product in the connection.
        child_uom (CharField): The unit of measure of the child product in the connection.
        child_quantity (DecimalField): The quantity of the child product in the connection.
    """

    # Display settings for the admin interface
    list_display = (
        "id",
        "parent_name",
        "parent_uom",
        "parent_quantity",
        "child_name",
        "child_uom",
        "child_quantity",
    ) + Change_Log.list_display
    search_fields = (
        "parent__name__icontains",
        "child__name__icontains",
    )
    list_filter = (
        "parent__name",
        "child__name",
    ) + Change_Log.list_filter

    def parent_name(self, obj):
        """
        Method to display the name of the parent product.

        Args:
            obj: The object representing the product connection.

        Returns:
            str: The name of the parent product.
        """
        return obj.parent.name

    def parent_uom(self, obj):
        """
        Method to display the unit of measure of the parent product.

        Args:
            obj: The object representing the product connection.

        Returns:
            str: The unit of measure of the parent product.
        """
        return obj.parent_uom.name

    def child_name(self, obj):
        """
        Method to display the name of the child product.

        Args:
            obj: The object representing the product connection.

        Returns:
            str: The name of the child product.
        """
        return obj.child.name

    def child_uom(self, obj):
        """
        Method to display the unit of measure of the child product.

        Args:
            obj: The object representing the product connection.

        Returns:
            str: The unit of measure of the child product.
        """
        return obj.child_uom.name

    def created(self, obj):
        """
        Method to handle the creation event for Product_Connection objects in the admin interface.

        Args:
            obj: The object representing the product connection.

        Returns:
            str: The creation details.
        """
        return super().created(PRODUCT_CONNECTION.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Product_Connection objects in the admin interface.

        Args:
            obj: The object representing the product connection.

        Returns:
            str: The change details.
        """
        return super().changed(PRODUCT_CONNECTION.objects.get(id=obj.id))
