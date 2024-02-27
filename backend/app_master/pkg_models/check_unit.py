# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class UNIT(CHANGE_LOG):
    """
    UNIT information
    """

    class Meta:
        verbose_name = "Unit"
        verbose_name_plural = "Units"
        ordering = ["name"]

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(UNIT, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} - {}".format(
            self.id, self.UNIT_CHOICES[self.unit][1], self.name
        )
