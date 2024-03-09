# Generated by Django 4.2 on 2024-03-07 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0004_stock_date_created_stock_date_modified"),
        ("portfolio", "0003_portfolio_date_created_portfolio_date_modified_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stockportfolio",
            name="stock",
            field=models.ForeignKey(
                help_text="Stock",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stock_portfolio",
                to="stock.stock",
                verbose_name="Stock",
            ),
        ),
    ]