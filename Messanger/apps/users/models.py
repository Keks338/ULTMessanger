from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models

class CustomUser(AbstractUser):
    short_Desc = models.TextField(max_length=500, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default=' ')
    is_Blocked = models.BooleanField(default=False)
    blocked_Time = models.DateTimeField(auto_now=True)
    line_status = models.BooleanField(default=False)
    friend_list_id = ArrayField(ArrayField(models.IntegerField()), default=list)