# Generated by Django 4.2.7 on 2024-01-13 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationshipmanagement', '0012_alter_companycontactbasemodel_company_and_more'),
        ('storagemanagement', '0010_alter_storagemanagementbookinglistusersetting_supplieritem_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplieritembasemodel',
            name='supplieritem',
        ),
        migrations.AddField(
            model_name='supplieritembasemodel',
            name='companyitem',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplieritem_companyitem', to='relationshipmanagement.companyitembasemodel', verbose_name='Artikel'),
        ),
        migrations.AddField(
            model_name='supplieritembasemodel',
            name='delivery_time',
            field=models.IntegerField(blank=True, help_text='Lieferzeit in Tagen.', null=True, verbose_name='Lieferzeit'),
        ),
        migrations.AddField(
            model_name='supplieritembasemodel',
            name='storageitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplieritem_storageitem', to='storagemanagement.storageitem', verbose_name='Lagerartikel'),
        ),
        migrations.AddField(
            model_name='supplieritembasemodel',
            name='types',
            field=models.CharField(blank=True, choices=[('CH', 'Chemie'), ('ET', 'Ersatzteil'), ('SO', 'Sonstiges'), ('VM', 'Verbrauchsmaterial')], default='SO', help_text='Art des Artikels', max_length=3, null=True, verbose_name='Art'),
        ),
    ]