# Generated by Django 4.2 on 2024-03-04 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_alter_stock_country_alter_stock_industry_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Stock', 'verbose_name_plural': 'Stocks'},
        ),
        migrations.AlterField(
            model_name='stock',
            name='country',
            field=models.CharField(blank=True, help_text='Country', max_length=50, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='industry',
            field=models.CharField(blank=True, help_text='Industry', max_length=100, null=True, verbose_name='Industry'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='ipo_year',
            field=models.IntegerField(blank=True, help_text='IPO year', null=True, verbose_name='IPO Year'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(blank=True, help_text='Stock name', max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='sector',
            field=models.CharField(blank=True, help_text='Sector', max_length=100, null=True, verbose_name='Sector'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='symbol',
            field=models.CharField(help_text='Stock symbol', max_length=10, unique=True, verbose_name='Symbol'),
        ),
    ]
