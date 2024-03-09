# ========================================================================
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from utility.methods import get_current_ts
from app_master.pkg_models.master_company import COMPANY

# ========================================================================
# COMPANY_CODE_CHOICES = (
#     (0, "DEFAULT_DEV"),
#     (1, "DEFAULT_QAL"),
#     (2, "DEFAULT_PRE_PROD"),
#     # ==========================
#     (3, "Shyama Prasad Diagnostics"),
# )
#
# COMPANY = 0
# COMPANY_CODE = "company_code"


# ORDER_STATUS_CHOICES = (
#     (0, "IN_PROGRESS"),
#     (1, "PLACED"),
#     (3, "CANCELLED"),
# )
class BASE_MODEL_MANAGER(models.Manager):
    def filter(self, *args, **kwargs):
        return (
            super(BASE_MODEL_MANAGER, self)
            .get_queryset()
            .filter(*args, **kwargs, is_deleted=False)
        )

    def all(self, *args, **kwargs):
        return (
            super(BASE_MODEL_MANAGER, self)
            .get_queryset()
            .filter(*args, **kwargs, is_deleted=False)
        )

    def get(self, *args, **kwargs):
        data = (
            super(BASE_MODEL_MANAGER, self)
            .get_queryset()
            .filter(*args, **kwargs, is_deleted=False)
        )
        if len(data) <= 0:
            raise ObjectDoesNotExist
        else:
            return data[0]


class CHANGE_LOG(models.Model):
    company_code = models.ForeignKey(
        COMPANY,
        on_delete=models.CASCADE,
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

    object = objects = BASE_MODEL_MANAGER()

    @staticmethod
    def get_unique_together():
        return ("company_code",)

    @staticmethod
    def get_ordering():
        return (
            "company_code",
            "is_deleted",
        )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.created_on == 0:
            self.created_on = get_current_ts()
            if self.created_by in (None, ""):
                self.created_by = "DEV"
        else:
            self.changed_on = get_current_ts()
            if self.changed_by in (None, ""):
                self.changed_by = "DEV"
        super(CHANGE_LOG, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if "forced" in kwargs.keys() and kwargs["forced"] is True:
            super(CHANGE_LOG, self).delete()
        else:
            self.is_deleted = True
            super(CHANGE_LOG, self).save()
