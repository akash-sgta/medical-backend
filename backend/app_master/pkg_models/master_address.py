# ========================================================================
from django.db import models

from app_master.pkg_models.master_text import TEXT
from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_city import CITY

# ========================================================================


class ADDRESS(CHANGE_LOG):
    """
    Address information.

    Attributes:
        city (ForeignKey to CITY): The city associated with the address.
        additional_line (ForeignKey to TEXT): Additional line for the address.
        street (CharField): The street of the address.
        postal_code (CharField): The postal code of the address.
        latitude (DecimalField): The latitude coordinate of the address.
        longitude (DecimalField): The longitude coordinate of the address.
    """

    class Meta:
        # Metadata for the model
        db_table = "master_master_address"
        managed = True
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        ordering = CHANGE_LOG.get_ordering() + ("id",)

    # Primary key field
    id = models.BigAutoField(primary_key=True)

    # City associated with the address
    city = models.ForeignKey(
        CITY,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # Additional line for the address
    additional_line = models.ForeignKey(
        TEXT,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    # Street of the address
    street = models.CharField(max_length=128)

    # Postal code of the address
    postal_code = models.CharField(max_length=32)

    # Latitude coordinate of the address
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
    )

    # Longitude coordinate of the address
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to allow for custom logic before saving.
        """
        super(ADDRESS, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the address.
        """
        # Format and return the string representation
        return "[{}] {}".format(self.company_code, self.id)
