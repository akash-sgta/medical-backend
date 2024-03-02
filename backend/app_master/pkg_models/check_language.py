# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG


# ========================================================================
class LANGUAGE(CHANGE_LOG):
    class Meta:
        db_table = "master_check_language"
        managed = True
        verbose_name = "Language"
        verbose_name_plural = "Languages"
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
        super(LANGUAGE, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.company_code, self.eng_name)
