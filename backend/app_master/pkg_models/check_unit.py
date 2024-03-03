# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class UNIT(CHANGE_LOG):
    """
    A model to represent unit information.

    Attributes:
        name (CharField): The name of the unit.
    """

    class Meta:
        db_table = "master_check_unit"
        managed = True
        verbose_name = "Unit"
        verbose_name_plural = "Units"
        ordering = CHANGE_LOG.get_ordering() + ("name",)
        unique_together = CHANGE_LOG.get_unique_together() + ("name",)

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=32,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure name is always in uppercase before saving.
        """
        self.name = self.name.upper()
        super(UNIT, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the unit.
        """
        return "[{}] {}".format(self.company_code, self.name)
