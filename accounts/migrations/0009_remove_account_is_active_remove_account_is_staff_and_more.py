# Generated by Django 4.2.5 on 2023-09-20 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_account_lock_remove_account_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='account',
            name='lock',
            field=models.CharField(choices=[('Lock', True), ('UnLock', False)], default=True, max_length=10),
        ),
        migrations.AddField(
            model_name='account',
            name='status',
            field=models.CharField(choices=[('Active', True), ('Inactive', False)], default=True, max_length=10),
        ),
    ]
