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
        ordering = ["eng_name"]

    id = models.BigAutoField(primary_key=True)

    eng_name = models.CharField(max_length=32, unique=True)
    local_name = models.CharField(max_length=32, unique=True)

    def save(self, *args, **kwargs):
        self.eng_name = self.eng_name.upper()
        super(LANGUAGE, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.eng_name)
