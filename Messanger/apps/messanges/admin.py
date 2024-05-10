from django.contrib import admin
from .models import MessageText

@admin.register(MessageText)
class MessageTextAdmin(admin.ModelAdmin):
    list_display = ('Text', 'Message_Creation_Date', 'Message_Edit_Date')
    search_fields = ('Sender_Id', 'Receiver_Id', 'Message_Creation_Date', 'Message_Edit_Date')
