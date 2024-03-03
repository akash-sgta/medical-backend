# ========================================================================
from django.db import models

from app_cdn.pkg_models.master_file import FILE
from app_master.pkg_models.master_text import TEXT
from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_product_type import PRODUCT_TYPE
from app_master.pkg_models.check_currency import CURRENCY

# ========================================================================


class PRODUCT(CHANGE_LOG):
    """
    Product information.

    Attributes:
        type (ForeignKey to PRODUCT_TYPE): The type of the product.
        image_01 (ForeignKey to FILE): The first image associated with the product.
        image_02 (ForeignKey to FILE): The second image associated with the product.
        image_03 (ForeignKey to FILE): The third image associated with the product.
        currency (ForeignKey to CURRENCY): The currency used for pricing the product.
        description (ForeignKey to TEXT): Description of the product.
        storage_instructions (ForeignKey to TEXT): Storage instructions for the product.
        side_effects (ForeignKey to TEXT): Side effects associated with the product.
        warnings_precautions (ForeignKey to TEXT): Warnings and precautions for the product.
        contraindications (ForeignKey to TEXT): Contraindications for the product.
        name (CharField): The name of the product.
        manufacturer (CharField): The manufacturer of the product.
        dosage (CharField): The dosage information for the product.
        price (DecimalField): The price of the product.
        url (URLField): The URL of the product.
        is_prescription_required (BooleanField): Indicates whether a prescription is required for the product.
    """

    class Meta:
        # Metadata for the model
        db_table = "master_master_product"
        managed = True
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = CHANGE_LOG.get_ordering() + (
            "type",
            "name",
        )
        unique_together = CHANGE_LOG.get_unique_together() + (
            "type",
            "name",
        )

    # Primary key field
    id = models.BigAutoField(primary_key=True)

    # Foreign key fields
    type = models.ForeignKey(PRODUCT_TYPE, on_delete=models.SET_NULL, null=True)
    image_01 = models.ForeignKey(
        FILE, on_delete=models.SET_NULL, related_name="image_01", null=True, blank=True
    )
    image_02 = models.ForeignKey(
        FILE, on_delete=models.SET_NULL, related_name="image_02", null=True, blank=True
    )
    image_03 = models.ForeignKey(
        FILE, on_delete=models.SET_NULL, related_name="image_03", null=True, blank=True
    )
    currency = models.ForeignKey(
        CURRENCY, on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.ForeignKey(
        TEXT,
        on_delete=models.SET_NULL,
        related_name="description",
        null=True,
        blank=True,
    )
    storage_instructions = models.ForeignKey(
        TEXT,
        on_delete=models.SET_NULL,
        related_name="storage_instructions",
        null=True,
        blank=True,
    )
    side_effects = models.ForeignKey(
        TEXT,
        on_delete=models.SET_NULL,
        related_name="side_effects",
        null=True,
        blank=True,
    )
    warnings_precautions = models.ForeignKey(
        TEXT,
        on_delete=models.SET_NULL,
        related_name="warnings_precautions",
        null=True,
        blank=True,
    )
    contraindications = models.ForeignKey(
        TEXT,
        on_delete=models.SET_NULL,
        related_name="contraindications",
        null=True,
        blank=True,
    )

    # Other fields
    name = models.CharField(max_length=32)
    manufacturer = models.CharField(max_length=128)
    dosage = models.CharField(max_length=64)
    price = models.DecimalField(default=0.0, max_digits=15, decimal_places=2)
    url = models.URLField(blank=True, null=True)
    is_prescription_required = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure name is always in uppercase before saving.
        If currency is not provided, it defaults to the first currency in the database.
        """
        self.name = self.name.upper()
        if self.currency is None:
            self.currency = CURRENCY.objects.get(id=1)
        super(PRODUCT, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the product.
        """
        return "[{}] {} -> {}".format(self.company_code, self.type, self.name)
