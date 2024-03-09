from django.contrib import admin
from django.urls import path
from . import views

app_name = "stock"

urlpatterns = [
    path("symbols/", views.get_nasdaq_symbols, name="stock-symbols"),
    path("upload-csv/", views.upload_csv, name="upload_csv"),
    path("finance/<str:symbol>/", views.get_stock_info, name="stock-info"),
]
