# ========================================================================
from django.db import models

from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.master_text import TEXT

# ========================================================================


class PRODUCT_TYPE(CHANGE_LOG):
    class Meta:
        db_table = "master_check_product_type"
        managed = True
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"
        ordering = ["name"]
        unique_together = ("name",) + CHANGE_LOG().get_unique_together()

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=32,
    )

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(PRODUCT_TYPE, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {}".format(self.id, self.name)


class PRODUCT_TYPE_T(CHANGE_LOG):
    class Meta:
        verbose_name = "Product Type Text"
        verbose_name_plural = "Product Type Texts"
        ordering = ["type", "text"]
        unique_together = ("type", "text") + CHANGE_LOG().get_unique_together()

    id = models.BigAutoField(
        primary_key=True,
    )

    type = models.ForeignKey(
        PRODUCT_TYPE,
        on_delete=models.CASCADE,
    )
    text = models.ForeignKey(
        TEXT,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super(PRODUCT_TYPE_T, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.req_type.name, self.text.lang.eng_name)
