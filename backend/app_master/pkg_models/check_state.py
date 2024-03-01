# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_country import COUNTRY

# ========================================================================


class STATE(CHANGE_LOG):
    """
    State information
    """

    class Meta:
        db_table = "master_check_state"
        managed = True
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["eng_name"]
        unique_together = ("country", "eng_name") + CHANGE_LOG().get_unique_together()

    id = models.BigAutoField(
        primary_key=True,
    )

    country = models.ForeignKey(
        COUNTRY,
        on_delete=models.CASCADE,
    )

    eng_name = models.CharField(
        max_length=128,
    )
    local_name = models.CharField(
        max_length=128,
    )

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.upper()
        super(STATE, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.country.eng_name, self.eng_name)
