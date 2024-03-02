# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG


# ========================================================================
class FILE_TYPE(CHANGE_LOG):
    class Meta:
        db_table = "cdn_check_file_type"
        managed = True
        verbose_name = "File Type"
        verbose_name_plural = "File Types"
        ordering = ["name"]
        unique_together = CHANGE_LOG.get_unique_together() + ("name",)

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=8,
    )

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(FILE_TYPE, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.company_code, self.name)
