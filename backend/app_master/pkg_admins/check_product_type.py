# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_product_type import PRODUCT_TYPE, PRODUCT_TYPE_T


# ========================================================================
class Product_Type(Change_Log):
    """
    Customizes the Django admin interface for managing product types.

    Attributes:
        name (CharField): The name of the product type.
    """

    # Display settings for the admin interface
    list_display = ("name",) + Change_Log.list_display
    search_fields = ("name__icontains",)
    list_filter = ("name",) + Change_Log.list_filter

    def created(self, obj):
        """
        Method to handle the creation event for Product_Type objects in the admin interface.

        Args:
            obj: The object representing the product type.

        Returns:
            str: The creation details.
        """
        return super().created(PRODUCT_TYPE.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Product_Type objects in the admin interface.

        Args:
            obj: The object representing the product type.

        Returns:
            str: The change details.
        """
        return super().changed(PRODUCT_TYPE.objects.get(id=obj.id))


class Product_Type_T(Change_Log):
    """
    Customizes the Django admin interface for managing translated product types.

    Attributes:
        type_name (CharField): The name of the product type.
        language (CharField): The language of the translation.
        description (CharField): The description of the translation.
    """

    # Display settings for the admin interface
    list_display = (
        "id",
        "type_name",
        "language",
        "description",
    ) + Change_Log.list_display
    list_filter = ("type__name",)
    search_fields = ("type__name__icontains",)

    def type_name(self, obj):
        """
        Method to display the name of the product type.

        Args:
            obj: The object representing the translated product type.

        Returns:
            str: The name of the product type.
        """
        return obj.type.name

    def language(self, obj):
        """
        Method to display the language of the translation.

        Args:
            obj: The object representing the translated product type.

        Returns:
            str: The language of the translation.
        """
        return obj.text.lang.eng_name

    def description(self, obj):
        """
        Method to display a truncated description of the translation.

        Args:
            obj: The object representing the translated product type.

        Returns:
            str: The truncated description.
        """
        return "{}...".format(obj.text.text[:32])

    def created(self, obj):
        """
        Method to handle the creation event for Product_Type_T objects in the admin interface.

        Args:
            obj: The object representing the translated product type.

        Returns:
            str: The creation details.
        """
        return super().created(PRODUCT_TYPE_T.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Product_Type_T objects in the admin interface.

        Args:
            obj: The object representing the translated product type.

        Returns:
            str: The change details.
        """
        return super().changed(PRODUCT_TYPE_T.objects.get(id=obj.id))
