# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG


# ========================================================================
class FILE_TYPE(CHANGE_LOG):
    """
    A model to represent file types.

    Attributes:
        name (CharField): The name of the file type.
    """

    class Meta:
        """
        Meta class for defining model metadata.
        """
        db_table = "cdn_check_file_type"
        managed = True
        verbose_name = "File Type"
        verbose_name_plural = "File Types"
        ordering = ["name"]
        unique_together = CHANGE_LOG.get_unique_together() + ("name",)

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=8,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure name is always in uppercase before saving.
        """
        self.name = self.name.upper()
        super(FILE_TYPE, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the file type.
        """
        return "[{}] {}".format(self.company_code, self.name)
