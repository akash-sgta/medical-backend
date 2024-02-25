# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class UOM(CHANGE_LOG):
    """
    UOM information
    """

    UNIT_CHOICES = [
        (0, None),
        (1, "Length"),
        (2, "Area"),
        (3, "Volume"),
        (4, "Mass"),
        (5, "Weight"),
        (6, "Temperature"),
        (7, "Density"),
    ]

    class Meta:
        verbose_name = "UOM"
        verbose_name_plural = "UOMs"
        ordering = ["eng_name"]
        unique_together = ("eng_name", "continent")

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=128, unique=True)
    unit = models.SmallIntegerField(default=0, choices=UNIT_CHOICES)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(UOM, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} - {}".format(
            self.id, self.UNIT_CHOICES[self.unit][1], self.name
        )
