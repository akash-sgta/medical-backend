# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from utility.methods import get_current_ts
from utility.abstract_view import View


# ========================================================================
class BASE_MODEL_MANAGERX(models.Manager):
    def filter(self, *args, **kwargs):
        if "forced" in kwargs.keys() and kwargs["forced"] is True:
            return (
                super(BASE_MODEL_MANAGERX, self)
                .get_queryset()
                .filter(
                    *args,
                    **kwargs,
                )
            )
        else:
            return (
                super(BASE_MODEL_MANAGERX, self)
                .get_queryset()
                .filter(
                    is_deleted=False,
                    *args,
                    **kwargs,
                )
            )

    def all(self, *args, **kwargs):
        if "forced" in kwargs.keys() and kwargs["forced"] is True:
            return (
                super(BASE_MODEL_MANAGERX, self)
                .get_queryset()
                .filter(
                    *args,
                    **kwargs,
                )
            )
        else:
            return (
                super(BASE_MODEL_MANAGERX, self)
                .get_queryset()
                .filter(
                    is_deleted=False,
                    *args,
                    **kwargs,
                )
            )

    def get(self, *args, **kwargs):
        data = (
            super(BASE_MODEL_MANAGERX, self)
            .get_queryset()
            .filter(*args, **kwargs, is_deleted=False)
        )
        if len(data) <= 0:
            raise ObjectDoesNotExist
        else:
            return data[0]


class COMPANY(models.Model):
    """
    A model to represent company information.

    Attributes:
        name (CharField): The name of the company in English.
    """

    class Meta:
        db_table = "master_master_company"
        managed = True
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ("id",)

    id = models.BigAutoField(
        primary_key=True,
    )

    name = models.CharField(
        max_length=32,
        unique=True,
    )
    created_on = models.FloatField(
        default=0,
        blank=True,
    )
    changed_on = models.FloatField(
        default=0,
        blank=True,
    )
    created_by = models.CharField(
        default="DEMO",
        max_length=16,
        blank=True,
    )
    changed_by = models.CharField(
        default="DEMO",
        max_length=16,
        blank=True,
    )
    is_deleted = models.BooleanField(
        default=False,
    )

    objects = BASE_MODEL_MANAGERX()

    def save(self, *args, **kwargs):
        """
        Overrides the save method to ensure name is always in uppercase before saving.
        """
        self.name = self.name.upper()
        if self.created_on == 0:
            self.created_on = get_current_ts()
            if self.created_by in (None, ""):
                self.created_by = "DEV"
        else:
            self.changed_on = get_current_ts()
            if self.changed_by in (None, ""):
                self.changed_by = "DEV"
        super(COMPANY, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if "forced" in kwargs.keys() and kwargs["forced"] is True:
            super(COMPANY, self).delete()
        else:
            self.is_deleted = True
            super(COMPANY, self).save()

    def __str__(self):
        """
        Returns a string representation of the company.
        """
        return "[{}] {}".format(self.id, self.name)
