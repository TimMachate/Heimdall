# Generated by Django 4.2.2 on 2023-11-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagemanagement', '0006_alter_offerdatabasemodel_recived_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdatabasemodel',
            name='authorized_datetime',
            field=models.DateTimeField(blank=True, default=None, editable=False, help_text='Zeitpunkt der Autorisierung.', null=True, verbose_name='Zeitpunkt der Autorisierung.'),
        ),
    ]
