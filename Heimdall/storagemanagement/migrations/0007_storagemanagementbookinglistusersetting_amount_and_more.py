# Generated by Django 4.2.7 on 2024-01-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagemanagement', '0006_storagebasemodel_unload'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagemanagementbookinglistusersetting',
            name='amount',
            field=models.BooleanField(default=True, help_text='Darstellung der Menge', verbose_name='Menge'),
        ),
        migrations.AddField(
            model_name='storagemanagementbookinglistusersetting',
            name='value',
            field=models.BooleanField(default=True, help_text='Darstellung des Wertes', verbose_name='Wert'),
        ),
        migrations.AddField(
            model_name='storagemanagementbookingtableusersetting',
            name='amount',
            field=models.BooleanField(default=True, help_text='Darstellung der Menge', verbose_name='Menge'),
        ),
        migrations.AddField(
            model_name='storagemanagementbookingtableusersetting',
            name='value',
            field=models.BooleanField(default=True, help_text='Darstellung des Wertes', verbose_name='Wert'),
        ),
    ]