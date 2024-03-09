from django.db import models
from services.common.mixins import DateFieldsMixin

from stock.models import Stock
from transactions.models import StockTransaction

NULLABLE = {"null": True, "blank": True}


# Create your models here.
class Portfolio(DateFieldsMixin, models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Name", help_text="Name", unique=True
    )
    description = models.TextField(
        verbose_name="Description", help_text="Description", **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class StockPortfolio(DateFieldsMixin, models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name="stock_portfolio",
        verbose_name="Portfolio",
        help_text="Portfolio",
    )
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name="stock_portfolio",
        verbose_name="Stock",
        help_text="Stock",
    )
    quantity = models.IntegerField(
        verbose_name="Quantity", help_text="Number of shares"
    )
    price_per_share = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price per share",
        help_text="Price per share",
        default=0.0,
    )
    purchase_date = models.DateField(
        verbose_name="Purchase Date", help_text="Purchase date", **NULLABLE
    )

    def __str__(self):
        return self.stock

    class Meta:
        unique_together = ("portfolio", "stock")
        verbose_name = "Stock Portfolio"
        verbose_name_plural = "Stock Portfolios"

    def calculate_quantity(self):
        transactions = StockTransaction.objects.filter(portfolio=self.portfolio)
        total_quantity = sum(transaction.shares for transaction in transactions)
        self.quantity = total_quantity

    def calculate_price_per_share(self):
        transactions = StockTransaction.objects.filter(portfolio=self.portfolio)
        total_price = sum(transaction.price for transaction in transactions)
        self.price_per_share = total_price / self.quantity
