from django import forms

from services.common.mixins import FormStyleMixin
from .models import Portfolio, StockPortfolio


class PortfolioForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class StockPortfolioForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = StockPortfolio
        fields = [
            "portfolio",
            "stock",
            "quantity",
            "price_per_share",
            "purchase_date",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
