# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.text import TEXT


# ========================================================================


class REQUIREMENT_TYPE(CHANGE_LOG):
    class Meta:
        verbose_name = "Requirement Type"
        verbose_name_plural = "Requirement Types"
        ordering = ["name"]

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=64, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(REQUIREMENT_TYPE, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class REQUIREMENT_TYPE_T(CHANGE_LOG):
    class Meta:
        verbose_name = "Requirement Type Text"
        verbose_name_plural = "Requirement Type Texts"
        ordering = ["req_type", "text"]
        unique_together = ("req_type", "text")

    id = models.BigAutoField(primary_key=True)
    req_type = models.ForeignKey(REQUIREMENT_TYPE, on_delete=models.CASCADE)
    text = models.ForeignKey(TEXT, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(REQUIREMENT_TYPE_T, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.req_type.name, self.text.lang.eng_name)
