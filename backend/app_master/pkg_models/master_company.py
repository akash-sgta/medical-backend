# ========================================================================
from django.db import models

from utility.methods import get_current_ts


# ========================================================================


class COMPANY(models.Model):
    """
    A model to represent company information.

    Attributes:
        name (CharField): The name of the company in English.
    """

    class Meta:
        db_table = "master_master_company"
        managed = True
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ("id",)

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=32,
        unique=True,
    )
    created_on = models.FloatField(
        default=0,
        blank=True,
    )
    changed_on = models.FloatField(
        default=0,
        blank=True,
    )
    created_by = models.CharField(
        default="DEMO",
        max_length=16,
        blank=True,
    )
    changed_by = models.CharField(
        default="DEMO",
        max_length=16,
        blank=True,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure name is always in uppercase before saving.
        """
        self.name = self.name.upper()
        if self.created_on == 0:
            self.created_on = get_current_ts()
        else:
            self.changed_on = get_current_ts()
        super(COMPANY, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the company.
        """
        return "[{}] {}".format(self.id, self.name)
