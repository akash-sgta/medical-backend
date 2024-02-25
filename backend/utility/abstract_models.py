# ========================================================================
from django.db import models
from utility.methods import get_current_ts


# ========================================================================


class CHANGE_LOG(models.Model):
    created_on = models.FloatField(default=0, blank=True)
    changed_on = models.FloatField(default=0, blank=True)
    created_by = models.CharField(default="DEMO", max_length=16, blank=True)
    changed_by = models.CharField(default="DEMO", max_length=16, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.created_on == 0:
            self.created_on = get_current_ts()
        else:
            self.changed_on = get_current_ts()
        super(CHANGE_LOG, self).save(*args, **kwargs)
