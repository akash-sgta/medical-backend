# ========================================================================
from django.core.validators import RegexValidator
from django.db import models

from app_cdn.pkg_models.master_file import FILE
from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.master_credential import CREDENTIAL
from app_master.pkg_models.master_address import ADDRESS
from app_master.pkg_models.master_text import TEXT

# ========================================================================


class PROFILE(CHANGE_LOG):
    """
    Profile information
    """

    class Meta:
        db_table = "master_master_profile"
        managed = True
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = CHANGE_LOG.get_ordering() + ("cred",)
        unique_together = CHANGE_LOG.get_unique_together() + ("cred",)

    id = models.BigAutoField(
        primary_key=True,
    )

    cred = models.OneToOneField(
        CREDENTIAL,
        on_delete=models.CASCADE,
    )
    address = models.OneToOneField(
        ADDRESS,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    image = models.ForeignKey(
        FILE,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    bio = models.ForeignKey(
        TEXT,
        on_delete=models.SET_NULL,
        related_name="bio",
        null=True,
        blank=True,
    )

    first_name = models.CharField(
        max_length=128,
    )
    middle_name = models.CharField(
        max_length=128,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=128,
    )
    phone_number = models.CharField(
        max_length=32,
        validators=[
            RegexValidator(
                regex="^\+(?:[0-9] ?){6,14}[0-9]$",
                message="Use format +91 4567890120.",
            )
        ],
        null=True,
        blank=True,
    )
    date_of_birth = models.CharField(
        max_length=8,  # YYYYMMDD
        validators=[
            RegexValidator(
                regex="^[1-9]{1}[0-9]{7}$",
                message="Use format YYYYMMDD.",
            )
        ],
    )
    facebook_profile = models.URLField(
        max_length=256,
        blank=True,
    )
    twitter_profile = models.URLField(
        max_length=256,
        blank=True,
    )
    linkedin_profile = models.URLField(
        max_length=256,
        blank=True,
    )

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper()
        self.middle_name = self.middle_name.upper()
        self.last_name = self.last_name.upper()
        super(PROFILE, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} -> {}.{}".format(
            self.company_code, self.cred, self.first_name, self.last_name
        )
