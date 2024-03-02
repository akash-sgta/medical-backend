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
        ordering = CHANGE_LOG.get_ordering() + ("eng_name",)
        unique_together = CHANGE_LOG.get_unique_together() + (
            "code",
            "eng_name",
        )

    id = models.BigAutoField(
        primary_key=True,
    )

    code = models.CharField(
        max_length=4,
    )
    eng_name = models.CharField(
        max_length=32,
    )
    local_name = models.CharField(
        max_length=32,
    )
    symbol = models.CharField(
        max_length=4,
    )

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.upper()
        self.code = self.code.upper()
        super(CURRENCY, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} - {}".format(self.company_code, self.code, self.eng_name)
