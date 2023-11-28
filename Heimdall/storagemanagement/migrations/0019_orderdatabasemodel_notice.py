# Generated by Django 4.2.2 on 2023-11-13 21:13

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('storagemanagement', '0018_alter_offerdatabasemodel_authorized_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdatabasemodel',
            name='notice',
            field=tinymce.models.HTMLField(blank=True, help_text='Nützliche Informationen für das Angebot.', null=True, verbose_name='Bemerkung'),
        ),
    ]