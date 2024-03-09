# ========================================================================
from django.db import models

from app_master.pkg_models.check_language import LANGUAGE
from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.master_text import TEXT

# ========================================================================


class PRODUCT_TYPE(CHANGE_LOG):
    """
    A model to represent product types.

    Attributes:
        name (CharField): The name of the product type.
    """

    class Meta:
        db_table = "master_check_product_type"
        managed = True
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"
        ordering = CHANGE_LOG.get_ordering() + ("name",)
        unique_together = CHANGE_LOG.get_unique_together() + ("name",)

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=32,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure name is always in uppercase before saving.
        """
        self.name = self.name.upper()
        super(PRODUCT_TYPE, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the product type.
        """
        return "[{}] {}".format(self.company_code, self.name)


class PRODUCT_TYPE_T(CHANGE_LOG):
    """
    A model to represent translations of product types.

    Attributes:
        type (ForeignKey to PRODUCT_TYPE): The product type.
        lang (ForeignKey to LANGUAGE): The language of the translation.
        text (ForeignKey to TEXT): The translated text.
    """

    class Meta:
        db_table = "master_check_product_type_text"
        verbose_name = "Product Type Text"
        verbose_name_plural = "Product Type Texts"
        ordering = CHANGE_LOG.get_ordering() + (
            "type",
            "lang",
            "text",
        )
        unique_together = CHANGE_LOG.get_unique_together() + (
            "type",
            "lang",
            "text",
        )

    id = models.BigAutoField(
        primary_key=True,
    )

    type = models.ForeignKey(
        PRODUCT_TYPE,
        on_delete=models.CASCADE,
    )
    lang = models.ForeignKey(
        LANGUAGE,
        on_delete=models.CASCADE,
    )
    text = models.ForeignKey(
        TEXT,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        """
        Overrides the save method to customize behavior.
        """
        super(PRODUCT_TYPE_T, self).save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the product type translation.
        """
        return "[{}] {} - {}".format(
            self.company_code, self.type.name, self.lang.eng_name
        )
