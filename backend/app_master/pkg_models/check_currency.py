# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class CURRENCY(CHANGE_LOG):
    """
    Currency information
    """

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        ordering = ["eng_name"]
        unique_together = ("eng_name", "continent")

    id = models.BigAutoField(primary_key=True)

    eng_name = models.CharField(max_length=128, unique=True)
    local_name = models.CharField(max_length=128, unique=True)
    symbol = models.CharField(max_length=8)

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.upper()
        super(COUNTRY, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.symbol, self.eng_name)
