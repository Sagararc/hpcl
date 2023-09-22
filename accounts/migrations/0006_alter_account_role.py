# Generated by Django 4.2.5 on 2023-09-20 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_account_is_active_remove_account_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('HR', 'HR'), ('MIS', 'MIS'), ('WE', 'WE'), ('CITYMANAGER', 'CITYMANAGER'), ('SUPERVISOR', 'SUPERVISOR'), ('FWP', 'FWP')], default='Active', max_length=100),
        ),
    ]