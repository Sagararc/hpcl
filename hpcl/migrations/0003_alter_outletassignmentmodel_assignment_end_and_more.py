# Generated by Django 4.2.5 on 2023-09-20 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpcl', '0002_delete_userlogin_alter_attendancemodel_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outletassignmentmodel',
            name='assignment_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 22, 1, 40, 53, 311273)),
        ),
        migrations.AlterField(
            model_name='outletassignmentmodel',
            name='assignment_start',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 21, 1, 40, 53, 311273)),
        ),
    ]