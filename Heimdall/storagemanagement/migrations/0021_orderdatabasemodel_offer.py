# Generated by Django 4.2.2 on 2023-11-19 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storagemanagement', '0020_remove_orderbasemodel_confirmation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdatabasemodel',
            name='offer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_offer', to='storagemanagement.offer', verbose_name='Angebot'),
        ),
    ]
