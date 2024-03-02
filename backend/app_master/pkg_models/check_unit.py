# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class UNIT(CHANGE_LOG):
    """
    UNIT information
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
        self.name = self.name.upper()
        super(UNIT, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.company_code, self.name)
