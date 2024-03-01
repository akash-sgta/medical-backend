# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_unit import UNIT

# ========================================================================


class UOM(CHANGE_LOG):
    """
    UOM information
    """

    class Meta:
        db_table = "master_check_uom"
        managed = True
        verbose_name = "UOM"
        verbose_name_plural = "UOMs"
        ordering = CHANGE_LOG.get_ordering() + ("name",)
        unique_together = CHANGE_LOG.get_unique_together() + (
            "name",
            "unit",
        )

    id = models.BigAutoField(
        primary_key=True,
    )

    unit = models.ForeignKey(
        UNIT,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=128,
    )

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(UOM, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} -> {}".format(self.company_code, self.unit, self.name)
