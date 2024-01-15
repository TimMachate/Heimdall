# Generated by Django 4.2.7 on 2024-01-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagemanagement', '0016_rename_authorized_user_storagemanagementrequestdatalistusersetting_authorized_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagemanagementrequestdatalistusersetting',
            name='url_authorize_false',
            field=models.BooleanField(default=True, help_text='Darstellung des Ablehnen-Links', verbose_name='Ablehnen-Link'),
        ),
        migrations.AddField(
            model_name='storagemanagementrequestdatalistusersetting',
            name='url_authorize_true',
            field=models.BooleanField(default=True, help_text='Darstellung des Autorisieren-Links', verbose_name='Autorisieren-Link'),
        ),
    ]