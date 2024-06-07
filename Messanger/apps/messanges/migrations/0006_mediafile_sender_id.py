# Generated by Django 3.2 on 2024-06-07 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messanges', '0005_auto_20240607_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='Sender_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
