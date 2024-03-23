# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from utility.methods import plaintext_to_sha256


# ========================================================================


class CREDENTIAL(CHANGE_LOG):
    """
    Credential information.

    Attributes:
        email (EmailField): The email address associated with the credential.
        pwd (CharField): The password for the credential.
        is_admin (BooleanField): Indicates whether the credential has admin privileges.
        is_internal_user (BooleanField): Indicates whether the credential belongs to an internal user (employee).
        is_external_user (BooleanField): Indicates whether the credential belongs to an external user (customer).
    """

    class Meta:
        # Metadata for the model
        db_table = "master_master_credential"
        managed = True
        verbose_name = "Credential"
        verbose_name_plural = "Credentials"
        ordering = CHANGE_LOG.get_ordering() + ("id",)
        unique_together = CHANGE_LOG.get_unique_together() + ("email",)

    # Primary key field
    id = models.BigAutoField(primary_key=True)

    # Email address associated with the credential
    email = models.EmailField(unique=True)

    # Password for the credential
    pwd = models.CharField(max_length=256)

    # Indicates whether the credential has admin privileges
    is_admin = models.BooleanField(default=False)

    # Indicates whether the credential belongs to an internal user (employee)
    is_internal_user = models.BooleanField(default=False)

    # Indicates whether the credential belongs to an external user (customer)
    is_external_user = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure email is always in uppercase before saving.
        """
        self.email = self.email.upper()
        if self.pwd[:7] != "sha256_":
            self.pwd = "sha256_" + plaintext_to_sha256(self.pwd)
        super(CREDENTIAL, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the credential.
        """
        return "[{}] {}".format(self.company_code, self.email)
