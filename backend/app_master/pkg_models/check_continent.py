# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class CONTINENT(CHANGE_LOG):
    """
    Continent information
    """

    class Meta:
        db_table = "master_check_continent"
        managed = True
        verbose_name = "Continent"
        verbose_name_plural = "Continents"
        ordering = CHANGE_LOG.get_ordering() + ("eng_name",)
        unique_together = CHANGE_LOG.get_unique_together() + ("eng_name",)

    id = models.BigAutoField(
        primary_key=True,
    )

    eng_name = models.CharField(
        max_length=32,
    )
    local_name = models.CharField(
        max_length=32,
    )

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.upper()
        super(CONTINENT, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.company_code, self.eng_name)
