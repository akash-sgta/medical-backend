# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class COUNTRY(CHANGE_LOG):
    """
    Country information
    """

    class Meta:
        db_table = "master_check_country"
        managed = True
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["eng_name"]
        unique_together = (
            "continent",
            "eng_name",
        ) + CHANGE_LOG().get_unique_together()

    id = models.BigAutoField(
        primary_key=True,
    )

    continent = models.CharField(
        max_length=32,
    )
    eng_name = models.CharField(
        max_length=32,
    )
    local_name = models.CharField(
        max_length=32,
    )

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.upper()
        self.continent = self.continent.upper()
        super(COUNTRY, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.id, self.eng_name)
