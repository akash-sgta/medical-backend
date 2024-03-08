# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class SALES_ORDER_STATUS(CHANGE_LOG):
    """
    A model to represent order status information.

    Attributes:
        name (CharField): The name of the company in English.
    """

    class Meta:
        db_table = "master_check_sales_order_status"
        managed = True
        verbose_name = "Sales Order Status"
        verbose_name_plural = "Sales Order Status"
        ordering = CHANGE_LOG.get_ordering() + ("name",)
        unique_together = CHANGE_LOG.get_unique_together() + ("name",)

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure name is always in uppercase before saving.
        """
        self.name = self.name.upper()
        super(SALES_ORDER_STATUS, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the company.
        """
        return "[{}] {}".format(self.company_code.id, self.name)


class INVENTORY_ORDER_STATUS(CHANGE_LOG):
    """
    A model to represent order status information.

    Attributes:
        name (CharField): The name of the company in English.
    """

    class Meta:
        db_table = "master_check_inventory_order_status"
        managed = True
        verbose_name = "Inventory Order Status"
        verbose_name_plural = "Inventory Order Status"
        ordering = CHANGE_LOG.get_ordering() + ("name",)
        unique_together = CHANGE_LOG.get_unique_together() + ("name",)

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=32,
        unique=True,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure name is always in uppercase before saving.
        """
        self.name = self.name.upper()
        super(INVENTORY_ORDER_STATUS, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the company.
        """
        return "[{}] {}".format(self.company_code.id, self.name)
