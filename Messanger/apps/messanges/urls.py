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
    path('get_messages/<int:chat_id>/', views.get_messages, name='get_messages'),
    path('send_message/', views.send_message, name='send_message'),
    path('upload/', views.upload_file, name='upload_file'),
    # path('file_list/', views.file_list, name='file_list'),
]