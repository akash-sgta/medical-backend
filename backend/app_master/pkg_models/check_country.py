# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_continent import CONTINENT


# ========================================================================
class COUNTRY(CHANGE_LOG):
    """
    A model to represent country information.

    Attributes:
        continent (ForeignKey to CONTINENT): The continent to which the country belongs.
        eng_name (CharField): The name of the country in English.
        local_name (CharField): The local name of the country.
    """

    class Meta:
        db_table = "master_check_country"
        managed = True
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = CHANGE_LOG.get_ordering() + ("eng_name",)
        unique_together = CHANGE_LOG.get_unique_together() + (
            "continent",
            "eng_name",
        )

    id = models.BigAutoField(
        primary_key=True,
    )

    continent = models.ForeignKey(
        CONTINENT,
        on_delete=models.CASCADE,
    )
    eng_name = models.CharField(
        max_length=32,
    )
    local_name = models.CharField(
        max_length=32,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure eng_name is always in uppercase before saving.
        """
        self.eng_name = self.eng_name.upper()
        super(COUNTRY, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the country.
        """
        return "[{}] {} -> {}".format(
            self.company_code, self.continent.eng_name, self.eng_name
        )
