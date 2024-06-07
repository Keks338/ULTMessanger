# Generated by Django 3.2 on 2024-06-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messanges', '0003_auto_20240531_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('audio', models.FileField(blank=True, null=True, upload_to='audios/')),
            ],
        ),
    ]
