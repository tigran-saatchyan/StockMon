from django.db import models

from services.common.mixins import DateFieldsMixin

NULLABLE = {"null": True, "blank": True}


# Create your models here.
class StockTransaction(DateFieldsMixin, models.Model):
    TRANSACTION_TYPES = (
        ("BUY", "Buy"),
        ("SELL", "Sell"),
    )

    transaction_type = models.CharField(
        max_length=4,
        choices=TRANSACTION_TYPES,
        default="BUY",
        help_text="Transaction type",
        verbose_name="Type",
    )
    trade_date = models.DateField(
        verbose_name="Trade Date", help_text="Trade date"
        )
    shares = models.DecimalField(
        verbose_name="Shares",
        help_text="Number of shares",
        max_digits=16,
        decimal_places=10,
        default=0.0,
    )
    cost_per_share = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Cost per share",
        help_text="Cost per share",
    )
    commission = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        **NULLABLE,
        help_text="Commission in dollars",
        verbose_name="Commission",
    )
    notes = models.TextField(verbose_name="Notes", **NULLABLE)
    portfolio = models.ForeignKey(
        "portfolio.Portfolio",
        on_delete=models.CASCADE,
        related_name="stock_transactions",
        verbose_name="Portfolio",
        help_text="Portfolio",
    )

    def __str__(self):
        return f"{self.transaction_type} - {self.trade_date}"

    class Meta:
        verbose_name = "Stock Transaction"
        verbose_name_plural = "Stock Transactions"
