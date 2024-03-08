# ========================================================================
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

    def all(self, *args, **kwargs):
        if "forced" in kwargs.keys() and kwargs["forced"] is True:
            super(CHANGE_LOG, self).all(*args, **kwargs)
        else:
            kwargs["is_deleted"] = False
            super(CHANGE_LOG, self).filter(*args, **kwargs)

    def filter(self, *args, **kwargs):
        if "forced" in kwargs.keys() and kwargs["forced"] is True:
            super(CHANGE_LOG, self).filter(*args, **kwargs)
        else:
            kwargs["is_deleted"] = False
            super(CHANGE_LOG, self).filter(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.created_on == 0:
            self.created_on = get_current_ts()
        else:
            self.changed_on = get_current_ts()
        super(CHANGE_LOG, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if "forced" in kwargs.keys() and kwargs["forced"] is True:
            super(CHANGE_LOG, self).delete(*args, **kwargs)
        else:
            self.is_deleted = True
            super(CHANGE_LOG, self).save(*args, **kwargs)
