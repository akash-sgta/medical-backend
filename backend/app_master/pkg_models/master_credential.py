# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG

# ========================================================================


class CREDENTIAL(CHANGE_LOG):
    """
    Credential information
    """

    class Meta:
        db_table = "master_master_credential"
        managed = True
        verbose_name = "Credential"
        verbose_name_plural = "Credentials"
        ordering = CHANGE_LOG.get_ordering() + ("id",)
        unique_together = CHANGE_LOG.get_unique_together() + ("email",)

    id = models.BigAutoField(
        primary_key=True,
    )

    email = models.EmailField(
        unique=True,
    )
    pwd = models.CharField(
        max_length=256,
    )
    is_admin = models.BooleanField(
        default=False,
    )
    is_internal_user = models.BooleanField(
        default=False,
    )  # Employee
    is_external_user = models.BooleanField(
        default=False,
    )  # Customer

    def save(self, *args, **kwargs):
        self.email = self.email.upper()
        super(CREDENTIAL, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.company_code, self.email)
