# ========================================================================
from django.db import models

from app_master.pkg_models.check_unit_of_measurement import UOM
from utility.abstract_models import CHANGE_LOG
from app_master.pkg_models.master_product import PRODUCT
from app_master.pkg_models.master_credential import CREDENTIAL
from app_master.pkg_models.check_currency import CURRENCY
from app_master.pkg_models.check_order_status import SALES_ORDER_STATUS

# ========================================================================


class PRODUCT_SALES_SUMMARY(CHANGE_LOG):
    class Meta:
        db_table = "transaction_sales_and_distribution_product_sales_summary"
        verbose_name = "Product Sales Summary"
        verbose_name_plural = "Product Sales Summaries"
        ordering = CHANGE_LOG.get_ordering() + (
            "buyer",
            "-id",
        )
        unique_together = CHANGE_LOG.get_unique_together() + (
            "buyer",
            "id",
        )

    id = models.BigAutoField(
        primary_key=True,
    )
    buyer = models.ForeignKey(
        CREDENTIAL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales_buyer",
    )

    status = models.ForeignKey(
        SALES_ORDER_STATUS,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super(PRODUCT_SALES_SUMMARY, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} -> {}".format(self.company_code, self.buyer, self.id)


class PRODUCT_SALES_ITEM(CHANGE_LOG):
    class Meta:
        db_table = "transaction_sales_and_distribution_product_sales_item"
        verbose_name = "Product Sales Item"
        verbose_name_plural = "Product Sales Items"
        ordering = CHANGE_LOG.get_ordering() + (
            "summary",
            "-id",
        )
        unique_together = CHANGE_LOG.get_unique_together() + (
            "summary",
            "product",
        )

    id = models.BigAutoField(
        primary_key=True,
    )
    summary = models.ForeignKey(
        PRODUCT_SALES_SUMMARY,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        PRODUCT,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    currency = models.ForeignKey(
        CURRENCY,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    uom = models.ForeignKey(
        UOM,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    unit_price = models.FloatField(
        default=1,
    )
    quantity = models.IntegerField(
        default=1,
    )
    net_amt = models.FloatField(
        default=1,
    )
    tax_rate = models.FloatField(
        default=1,
    )

    def save(self, *args, **kwargs):
        if self.product is not None:
            self.net_amt = self.unit_price * self.quantity
        else:
            self.net_amt = 0
        if self.currency is None:
            self.currency = CURRENCY.objects.get(id=1)
        super(PRODUCT_SALES_ITEM, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} -> {}".format(self.company_code, self.summary, self.id)


class PRODUCT_SALES_REFERRAL(CHANGE_LOG):
    class Meta:
        db_table = "transaction_sales_and_distribution_product_sales_referral"
        verbose_name = "Product Sales Referral"
        verbose_name_plural = "Product Sales Referrals"
        ordering = CHANGE_LOG.get_ordering() + (
            "referral",
            "summary",
            "-id",
        )
        unique_together = CHANGE_LOG.get_unique_together() + (
            "summary",
            "referral",
        )

    id = models.BigAutoField(
        primary_key=True,
    )
    summary = models.ForeignKey(
        PRODUCT_SALES_SUMMARY,
        on_delete=models.CASCADE,
    )
    referral = models.ForeignKey(
        CREDENTIAL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales_referral",
    )

    def save(self, *args, **kwargs):
        super(PRODUCT_SALES_REFERRAL, self).save(*args, **kwargs)

    def __str__(self):
        return "[{}] {} -> {}".format(self.company_code, self.referral, self.id)
