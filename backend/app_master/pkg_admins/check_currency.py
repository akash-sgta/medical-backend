# ========================================================================
from utility.abstract_admin import Change_Log
from app_master.pkg_models.check_currency import CURRENCY


# ========================================================================
class Currency(Change_Log):
    """
    Customizes the Django admin interface for managing currencies.

    Attributes:
        code (CharField): The currency code.
        eng_name (CharField): The English name of the currency.
        local_name (CharField): The local name of the currency.
        symbol (CharField): The symbol of the currency.
    """

    # Display settings for the admin interface
    list_display = (
        "code",
        "eng_name",
        "local_name",
        "symbol",
    ) + Change_Log.list_display
    search_fields = (
        "code__icontains",
        "eng_name__icontains",
        "local_name__icontains",
        "symbol__icontains",
    )

    def created(self, obj):
        """
        Method to handle the creation event for Currency objects in the admin interface.

        Args:
            obj: The object representing the currency.

        Returns:
            str: The creation details.
        """
        return super().created(CURRENCY.objects.get(id=obj.id))

    def changed(self, obj):
        """
        Method to handle the change event for Currency objects in the admin interface.

        Args:
            obj: The object representing the currency.

        Returns:
            str: The change details.
        """
        return super().changed(CURRENCY.objects.get(id=obj.id))
