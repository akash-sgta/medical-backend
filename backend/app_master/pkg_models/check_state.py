# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_country import COUNTRY

# ========================================================================


class STATE(CHANGE_LOG):
    """
    A model to represent state information.

    Attributes:
        country (ForeignKey to COUNTRY): The country to which the state belongs.
        eng_name (CharField): The name of the state in English.
        local_name (CharField): The local name of the state.
    """

    class Meta:
        db_table = "master_check_state"
        managed = True
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = CHANGE_LOG.get_ordering() + ("eng_name",)
        unique_together = CHANGE_LOG.get_unique_together() + ("country", "eng_name")

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
        """
        Overrides the save method to ensure eng_name is always in uppercase before saving.
        """
        self.eng_name = self.eng_name.upper()
        super(STATE, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the state.
        """
        return "[{}] {} -> {}".format(self.company_code, self.country, self.eng_name)
