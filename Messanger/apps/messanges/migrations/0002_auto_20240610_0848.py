# Generated by Django 3.2 on 2024-06-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messanges', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='File_Creation_Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='messagetext',
            name='Message_Creation_Date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='messagetext',
            name='Message_Edit_Date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]