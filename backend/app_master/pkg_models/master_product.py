# ========================================================================
from django.db import models

from app_master.pkg_models.check_product_type import REQUIREMENT_TYPE
from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_product_type import PRODUCT_TYPE

# ========================================================================


class PRODUCT(CHANGE_LOG):
    """
    Product information
    """

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["type", "id"]

    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(PRODUCT_TYPE, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)
    manufacturer = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    formulation = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storage_instructions = models.TextField()
    side_effects = models.TextField()
    warnings_precautions = models.TextField()
    contraindications = models.TextField()
    is_prescription_required = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(PRODUCT, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)
