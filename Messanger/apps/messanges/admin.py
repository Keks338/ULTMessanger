from django.contrib import admin
from .models import MessageText, GroupChat, Chat

@admin.register(MessageText)
class MessageTextAdmin(admin.ModelAdmin):
    list_display = ('Text', 'Message_Creation_Date', 'Message_Edit_Date')
    search_fields = ('Sender_Id', 'Receiver_Id', 'Message_Creation_Date', 'Message_Edit_Date')

@admin.register(GroupChat)
class GroupChatAdmin(admin.ModelAdmin):
    list_display = ('Group_name', 'Group_desc', 'Users_list_id', 'Users_admin_list_id')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('User1', 'User2', 'Creation_date')