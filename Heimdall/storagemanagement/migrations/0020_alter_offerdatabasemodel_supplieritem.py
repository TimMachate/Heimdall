# Generated by Django 4.2.7 on 2024-01-13 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storagemanagement', '0019_remove_storagemanagementrequestdataoverviewusersetting_update_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerdatabasemodel',
            name='supplieritem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offerdata_supplieritem', to='storagemanagement.supplieritem', verbose_name='Firmenartikel'),
        ),
    ]
