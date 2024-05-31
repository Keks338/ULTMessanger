from django.db import models
from ..users.models import CustomUser
from django.contrib.postgres.fields import ArrayField
class Chat(models.Model):
    User1 = models.ForeignKey(CustomUser, related_name='first_user', null=True, blank=True, on_delete=models.CASCADE)
    User2 = models.ForeignKey(CustomUser, related_name='second_user', null=True, blank=True, on_delete=models.CASCADE)
    Creation_date = models.DateField(auto_now_add=True)

class GroupChat(models.Model):
    Users_list_id = ArrayField(ArrayField(models.IntegerField()), default=list)
    Users_admin_list_id = ArrayField(ArrayField(models.IntegerField()), default=list)
    Group_name = models.CharField(max_length=100)
    Group_desc = models.TextField(max_length=500)
class MessageText(models.Model):
    Chat_id = models.ForeignKey(Chat, null=True, blank=True, on_delete=models.CASCADE)
    Group_chat_id = models.ForeignKey(GroupChat, null=True, blank=True, on_delete=models.CASCADE)
    Text = models.TextField(max_length=500, blank=True)
    Sender = models.ForeignKey(CustomUser, related_name='sent_messages', null=True, blank=True, on_delete=models.CASCADE)
    Message_Creation_Date = models.DateField(auto_now_add=True)
    Message_Edit_Date = models.DateField(auto_now=True)