from django.contrib import admin
from django.urls import path
from pins import views

app_name = "pins"
urlpatterns = [
    path("", views.index, name="index"),
    path("change/<int:id>", views.change, name="change"),
    path("delete/<int:id>", views.delete, name="delete")
]
