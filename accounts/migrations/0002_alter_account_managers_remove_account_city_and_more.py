# Generated by Django 4.2.5 on 2023-09-20 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hpcl', '0002_delete_userlogin_alter_attendancemodel_user_and_more'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='city',
        ),
        migrations.AddField(
            model_name='account',
            name='cityName',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hpcl.citymodel'),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('HR', 'HR'), ('MIS', 'MIS'), ('WE', 'WE')], default='Active', max_length=100),
        ),
    ]
