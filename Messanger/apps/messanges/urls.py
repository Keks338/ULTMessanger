from django.urls import path

from . import views

app_name = "messanges"

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path('remove-friend/', views.remove_friend, name='removeFriend'),
    path('add-friend/', views.add_friend, name='addFriend'),
]