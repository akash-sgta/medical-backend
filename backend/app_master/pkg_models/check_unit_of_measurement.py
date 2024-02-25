# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class UOM(CHANGE_LOG):
    """
    UOM information
    """

    class Meta:
        verbose_name = "UOM"
        verbose_name_plural = "UOMs"
        ordering = ["eng_name"]
        unique_together = ("eng_name", "continent")

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=128, unique=True)
    local_name = models.CharField(max_length=128, unique=True)
    continent = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.upper()
        self.continent = self.continent.upper()
        super(UOM, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.id, self.eng_name)
