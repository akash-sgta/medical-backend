# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.master_product import PRODUCT
from app_master.pkg_models.check_unit_of_measurement import UOM

# ========================================================================


class PRODUCT_CONNECTION(CHANGE_LOG):
    """
    Product Connection information
    """

    class Meta:
        verbose_name = "Product Connection"
        verbose_name_plural = "Product Connections"
        ordering = ["parent", "child"]
        unique_together = ("parent_product", "child_product")

    id = models.BigAutoField(primary_key=True)
    parent = models.ForeignKey(
        PRODUCT, related_name="parent_product", on_delete=models.CASCADE
    )
    parent_uom = models.ForeignKey(
        UOM, related_name="parent_uom", on_delete=models.CASCADE
    )
    child = models.ForeignKey(
        PRODUCT, related_name="child_product", on_delete=models.CASCADE
    )
    child_uom = models.ForeignKey(
        UOM, related_name="child_uom", on_delete=models.CASCADE
    )

    parent_quantity = models.FloatField(default=1)
    child_quantity = models.FloatField(default=1)

    def save(self, *args, **kwargs):
        super(PRODUCT_CONNECTION, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)
