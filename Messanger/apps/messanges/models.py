from django.db import models
from ..users.models import CustomUser

class MessageText(models.Model):
    Text = models.TextField(max_length=500, blank=True)
    Sender = models.OneToOneField(CustomUser, related_name='sent_messages', null=True, blank=True, on_delete=models.CASCADE)
    Receiver = models.OneToOneField(CustomUser, related_name='received_messages', null=True, blank=True, on_delete=models.CASCADE)
    Message_Creation_Date = models.DateField(auto_now_add=True)
    Message_Edit_Date = models.DateField(auto_now=True)