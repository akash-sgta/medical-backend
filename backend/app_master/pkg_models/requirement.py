# ========================================================================
from django.db import models

from app_master.pkg_models.requirement_type import REQUIREMENT_TYPE
from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.text import TEXT


# ========================================================================


class REQUIREMENT(CHANGE_LOG):
    """
    REQUIREMENT information
    """

    class Meta:
        verbose_name = "Requirement"
        verbose_name_plural = "Requirements"
        ordering = ["type", "id"]

    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(
        REQUIREMENT_TYPE, on_delete=models.SET_NULL, null=True
    )

    name = models.CharField(max_length=128, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(REQUIREMENT, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class REQUIREMENT_T(CHANGE_LOG):
    class Meta:
        verbose_name = "Requirement Text"
        verbose_name_plural = "Requirement Texts"
        ordering = ["req", "text"]
        unique_together = ("req", "text")

    id = models.BigAutoField(primary_key=True)
    req = models.ForeignKey(REQUIREMENT, on_delete=models.CASCADE)
    text = models.ForeignKey(TEXT, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(REQUIREMENT_T, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.req.name, self.text.lang.eng_name)
