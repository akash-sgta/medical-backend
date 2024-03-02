# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_state import STATE

# ========================================================================


class CITY(CHANGE_LOG):
    """
    City information
    """

    class Meta:
        db_table = "master_check_city"
        managed = True
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = CHANGE_LOG.get_ordering() + ("eng_name",)
        unique_together = CHANGE_LOG.get_unique_together() + (
            "state",
            "eng_name",
        )

    id = models.BigAutoField(
        primary_key=True,
    )

    state = models.ForeignKey(
        STATE,
        on_delete=models.CASCADE,
    )

    eng_name = models.CharField(
        max_length=32,
    )
    local_name = models.CharField(
        max_length=32,
    )

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.upper()
        super(CITY, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} -> {}".format(
            self.company_code, self.state.eng_name, self.eng_name
        )
