# Generated by Django 4.2.2 on 2023-11-11 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storagemanagement', '0012_alter_offer_options_alter_orderdatabasemodel_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdatabasemodel',
            name='amount',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Menge'),
        ),
    ]
