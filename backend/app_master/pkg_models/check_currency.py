# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class CURRENCY(CHANGE_LOG):
    """
    Currency information
    """

    class Meta:
        db_table = "master_check_currency"
        managed = True
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        ordering = ["eng_name"]

    id = models.BigAutoField(primary_key=True)

    code = models.CharField(max_length=3, unique=True)
    eng_name = models.CharField(max_length=128, unique=True)
    local_name = models.CharField(max_length=128, unique=True)
    symbol = models.CharField(max_length=8)

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.upper()
        self.code = self.code.upper()
        super(CURRENCY, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} {}".format(self.id, self.symbol, self.eng_name)
