# ========================================================================
from django.db import models

from app_cdn.pkg_models.master_file import FILE
from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_product_type import PRODUCT_TYPE
from app_master.pkg_models.check_currency import CURRENCY

# ========================================================================


class PRODUCT(CHANGE_LOG):
    """
    Product information
    """

    class Meta:
        db_table = "master_master_product"
        managed = True
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = CHANGE_LOG.get_ordering() + (
            "type",
            "id",
        )
        unique_together = CHANGE_LOG.get_unique_together() + (
            "type",
            "name",
        )

    id = models.BigAutoField(
        primary_key=True,
    )

    type = models.ForeignKey(
        PRODUCT_TYPE,
        on_delete=models.SET_NULL,
        null=True,
    )
    image_01 = models.ForeignKey(
        FILE,
        on_delete=models.SET_NULL,
        related_name="image_01",
        null=True,
        blank=True,
    )
    image_02 = models.ForeignKey(
        FILE,
        on_delete=models.SET_NULL,
        related_name="image_02",
        null=True,
        blank=True,
    )
    image_03 = models.ForeignKey(
        FILE,
        on_delete=models.SET_NULL,
        related_name="image_03",
        null=True,
        blank=True,
    )
    currency = models.ForeignKey(
        CURRENCY,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    name = models.CharField(
        max_length=32,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    manufacturer = models.CharField(
        max_length=128,
    )
    dosage = models.CharField(
        max_length=64,
    )
    price = models.FloatField(
        default=0.0,
    )
    storage_instructions = models.TextField()
    side_effects = models.TextField()
    warnings_precautions = models.TextField()
    contraindications = models.TextField()
    url = models.URLField(
        blank=True,
        null=True,
    )
    is_prescription_required = models.BooleanField(
        default=False,
    )

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        if self.currency is None:
            self.currency = CURRENCY.objects.get(id=1)
        super(PRODUCT, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} -> {}".format(self.company_code, self.type, self.name)
