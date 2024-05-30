from django.urls import path

from . import views

app_name = "messanges"

urlpatterns = [
    path("", views.homePage, name="homePage"),
    path('remove-friend/', views.remove_friend, name='removeFriend'),
    path('remove-friend-p/', views.remove_friend_p, name='removeFriendP'),
    path('add-friend/', views.add_friend, name='addFriend'),
    path('add-chat/', views.add_chat, name='addChat'),
    path('remove-chat/', views.remove_chat, name='removeChat'),
]