# Generated by Django 4.2.7 on 2023-12-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationshipmanagement', '0004_alter_relationshipmanagementcompanylistusersetting_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_contact',
            new_name='contact',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_create_date',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_create_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_create_user',
            new_name='create_user',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_house_number',
            new_name='house_number',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_item',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_notice',
            new_name='notice',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_postcode',
            new_name='postcode',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_reference_number',
            new_name='reference_number',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_street',
            new_name='street',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_update_date',
            new_name='update_date',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_update_time',
            new_name='update_time',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_update_user',
            new_name='update_user',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_url_delete',
            new_name='url_delete',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_url_detail',
            new_name='url_detail',
        ),
        migrations.RenameField(
            model_name='relationshipmanagementcompanytableusersetting',
            old_name='company_table_url_update',
            new_name='url_update',
        ),
        migrations.AddField(
            model_name='relationshipmanagementcompanytableusersetting',
            name='api',
            field=models.CharField(default='relationshipmanagementAPI:company_list', help_text='Url Adresse der API', max_length=200, verbose_name='API Url'),
        ),
    ]
