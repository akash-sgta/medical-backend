# ========================================================================
from django.db import models

from app_cdn.pkg_models.file import FILE
from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.requirement import REQUIREMENT


# ========================================================================


class WORK_NOTE(CHANGE_LOG):
    class Meta:
        verbose_name = "Work Note"
        verbose_name_plural = "Work Notes"
        ordering = ["req", "-id"]

    id = models.BigAutoField(primary_key=True)
    req = models.ForeignKey(REQUIREMENT, on_delete=models.CASCADE)
    file = models.ForeignKey(FILE, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(WORK_NOTE, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)
