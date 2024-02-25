# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_cdn.pkg_models.check_file_type import FILE_TYPE


# ========================================================================


class FILE(CHANGE_LOG):
    """
    File information
    """

    class Meta:
        verbose_name = "File"
        verbose_name_plural = "Files"

    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(FILE_TYPE, on_delete=models.SET_NULL, null=True)
    size = models.FloatField(default=0)  # in Bytes
    name = models.CharField(max_length=128, unique=True)
    url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(FILE, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)
