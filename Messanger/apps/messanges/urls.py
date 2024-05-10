from django.urls import path

from . import views

app_name = "messanges"

urlpatterns = [
    path("", views.homePage, name="homePage"),
]