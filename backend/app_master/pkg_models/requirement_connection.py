# ========================================================================
from django.db import models

from app_master.pkg_models.requirement import REQUIREMENT
from utility.abstract_models import CHANGE_LOG


# ========================================================================


class REQUIREMENT_CONNECTION(CHANGE_LOG):
    """
    REQUIREMENT information
    """

    class Meta:
        verbose_name = "Requirement Connection"
        verbose_name_plural = "Requirement Connections"
        ordering = ["parent_req", "child_req"]
        unique_together = ("parent_req", "child_req")

    id = models.BigAutoField(primary_key=True)
    parent_req = models.ForeignKey(
        REQUIREMENT,
        related_name="parent",
        on_delete=models.CASCADE,
        null=True,
    )
    child_req = models.ForeignKey(
        REQUIREMENT,
        related_name="child",
        on_delete=models.CASCADE,
        null=True,
    )

    def save(self, *args, **kwargs):
        super(REQUIREMENT_CONNECTION, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.parent_req.id, self.child_req.id)
