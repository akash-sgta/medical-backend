# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_city import CITY

# ========================================================================


class ADDRESS(CHANGE_LOG):
    """
    Address information
    """

    class Meta:
        db_table = "master_master_address"
        managed = True
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        ordering = ["id"]

    id = models.BigAutoField(primary_key=True)

    city = models.ForeignKey(CITY, on_delete=models.SET_NULL, null=True, blank=True)

    street = models.CharField(max_length=128)
    postal_code = models.CharField(max_length=32)
    additional_line = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        super(ADDRESS, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}]".format(self.id)
