# Generated by Django 4.2.5 on 2023-09-22 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpcl', '0010_alter_outletassignmentmodel_assignment_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outletassignmentmodel',
            name='assignment_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 23, 14, 28, 19, 432815)),
        ),
        migrations.AlterField(
            model_name='outletassignmentmodel',
            name='assignment_start',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 14, 28, 19, 432815)),
        ),
    ]
