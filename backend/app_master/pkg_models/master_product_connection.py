# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.master_product import PRODUCT
from app_master.pkg_models.check_unit_of_measurement import UOM

# ========================================================================


class PRODUCT_CONNECTION(CHANGE_LOG):
    """
    Product Connection information.

    Attributes:
        parent (ForeignKey to PRODUCT): The parent product in the connection.
        parent_uom (ForeignKey to UOM): The unit of measure for the parent product.
        child (ForeignKey to PRODUCT): The child product in the connection.
        child_uom (ForeignKey to UOM): The unit of measure for the child product.
        parent_quantity (FloatField): The quantity of the parent product.
        child_quantity (FloatField): The quantity of the child product.
    """

    class Meta:
        db_table = "master_master_product_connection"
        managed = True
        verbose_name = "Product Connection"
        verbose_name_plural = "Product Connections"
        ordering = CHANGE_LOG.get_ordering() + (
            "parent",
            "child",
        )
        unique_together = CHANGE_LOG.get_unique_together() + (
            "parent",
            "child",
        )

    id = models.BigAutoField(primary_key=True)

    parent = models.ForeignKey(
        PRODUCT,
        related_name="parent_product",
        on_delete=models.CASCADE,
    )
    parent_uom = models.ForeignKey(
        UOM,
        related_name="parent_uom",
        on_delete=models.CASCADE,
    )
    child = models.ForeignKey(
        PRODUCT,
        related_name="child_product",
        on_delete=models.CASCADE,
    )
    child_uom = models.ForeignKey(
        UOM,
        related_name="child_uom",
        on_delete=models.CASCADE,
    )

    parent_quantity = models.FloatField(default=1)
    child_quantity = models.FloatField(default=1)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to save the object.
        """
        super(PRODUCT_CONNECTION, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the product connection.
        """
        return "[{}] {} - {}".format(
            self.company_code, self.parent.name, self.child.name
        )
