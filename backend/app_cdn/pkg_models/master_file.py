# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_cdn.pkg_models.check_file_type import FILE_TYPE


# ========================================================================


class FILE(CHANGE_LOG):
    """
    A model to represent file information.

    Attributes:
        type (ForeignKey to FILE_TYPE): The type of the file.
        name (CharField): The name of the file.
        size (FloatField): The size of the file in bytes.
        url (URLField): The URL of the file.
    """

    class Meta:
        db_table = "cdn_master_file"
        managed = True
        verbose_name = "File"
        verbose_name_plural = "Files"
        ordering = CHANGE_LOG.get_ordering() + (
            "type",
            "name",
        )
        unique_together = CHANGE_LOG.get_unique_together() + (
            "type",
            "name",
        )

    id = models.BigAutoField(
        primary_key=True,
    )

    type = models.ForeignKey(
        FILE_TYPE,
        on_delete=models.SET_NULL,
        null=True,
    )

    name = models.CharField(max_length=128)
    size = models.FloatField(
        default=0,
    )  # in Bytes
    url = models.URLField(
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure name is always in uppercase before saving.
        """
        self.name = self.name.upper()
        super(FILE, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the file.
        """
        return "[{}] {} -> {}".format(self.company_code, self.type, self.name)
