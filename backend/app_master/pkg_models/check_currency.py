# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG


# ========================================================================
class CURRENCY(CHANGE_LOG):
    """
    Currency information.

    Attributes:
        code (CharField): The currency code.
        eng_name (CharField): The name of the currency in English.
        local_name (CharField): The local name of the currency.
        symbol (CharField): The currency symbol.
    """

    class Meta:
        # Metadata for the model
        db_table = "master_check_currency"
        managed = True
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        ordering = CHANGE_LOG.get_ordering() + ("eng_name",)
        unique_together = CHANGE_LOG.get_unique_together() + (
            "code",
            "eng_name",
        )

    # Primary key field
    id = models.BigAutoField(primary_key=True)

    # Currency code
    code = models.CharField(max_length=4)

    # English name of the currency
    eng_name = models.CharField(max_length=32)

    # Local name of the currency
    local_name = models.CharField(max_length=32)

    # Currency symbol
    symbol = models.CharField(max_length=4)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure eng_name and code are always in uppercase before saving.
        """
        self.eng_name = self.eng_name.upper()  # Convert eng_name to uppercase
        self.code = self.code.upper()  # Convert code to uppercase
        super(CURRENCY, self).save(*args, **kwargs)  # Call parent class's save method

    def __str__(self):
        """
        Returns a string representation of the currency.
        """
        # Format and return the string representation
        return "[{}] {} - {}".format(self.company_code, self.code, self.eng_name)
