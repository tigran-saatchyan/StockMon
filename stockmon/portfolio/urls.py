from django.contrib import admin
from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("create/", views.CreateView.as_view(), name="create-portfolio"),
    path("list/", views.ListView.as_view(), name="list-portfolio"),
    path("detail/<int:pk>", views.DetailView.as_view(), name="detail-portfolio"),
    path("update/<int:pk>", views.UpdateView.as_view(), name="update-portfolio"),
    path("delete/<int:pk>", views.DeleteView.as_view(), name="delete-portfolio"),
]
