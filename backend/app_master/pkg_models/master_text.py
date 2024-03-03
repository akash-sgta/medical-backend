# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.check_language import LANGUAGE


# ========================================================================
class TEXT(CHANGE_LOG):
    """
    Text information.

    Attributes:
        text (TextField): The text content.
    """

    class Meta:
        db_table = "master_master_text"
        managed = True
        verbose_name = "Text"
        verbose_name_plural = "Texts"
        ordering = CHANGE_LOG.get_ordering()

    id = models.BigAutoField(primary_key=True)
    text = models.TextField()

    def save(self, *args, **kwargs):
        """
        Overrides the save method to save the text instance.
        """
        super(TEXT, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the text, truncated to the first 8 characters.
        """
        return "[{}] {}...".format(self.company_code, self.text[:8])
