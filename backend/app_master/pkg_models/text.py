# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.language import LANGUAGE


# ========================================================================
class TEXT(CHANGE_LOG):
    class Meta:
        verbose_name = "Text"
        verbose_name_plural = "Texts"
        ordering = ["lang"]
        unique_together = ("id", "lang")

    id = models.BigAutoField(primary_key=True)
    lang = models.ForeignKey(LANGUAGE, on_delete=models.CASCADE)
    text = models.TextField()

    def save(self, *args, **kwargs):
        super(TEXT, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}...".format(self.lang.eng_name, self.text[:32])
