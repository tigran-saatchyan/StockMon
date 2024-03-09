from django.db import models
import csv
from io import TextIOWrapper

from services.common.mixins import DateFieldsMixin

NULLABLE = {"null": True, "blank": True}


class Stock(DateFieldsMixin, models.Model):
    symbol = models.CharField(
        max_length=10, unique=True, verbose_name="Symbol", help_text="Stock symbol"
    )
    name = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Name", help_text="Stock name"
    )
    country = models.CharField(
        max_length=50, **NULLABLE, verbose_name="Country", help_text="Country"
    )
    ipo_year = models.IntegerField(
        **NULLABLE, verbose_name="IPO Year", help_text="IPO year"
    )
    sector = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Sector", help_text="Sector"
    )
    industry = models.CharField(
        max_length=100, **NULLABLE, verbose_name="Industry", help_text="Industry"
    )

    @classmethod
    def create_from_csv(cls, csv_file):
        file = TextIOWrapper(csv_file.file, encoding="utf-8")
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            symbol, name, country, ipo_year, sector, industry = row

            try:
                ipo_year = int(ipo_year)
            except ValueError:
                ipo_year = None
            stock = cls(
                symbol=symbol,
                name=name,
                country=country,
                ipo_year=ipo_year,
                sector=sector,
                industry=industry,
            )
            stock.save()
        file.close()

    def __str__(self):
        return self.symbol

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
