# Generated by Django 4.2.5 on 2023-09-20 20:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpcl', '0005_alter_outletassignmentmodel_assignment_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outletassignmentmodel',
            name='assignment_end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 9, 22, 2, 21, 36, 162839)),
        ),
        migrations.AlterField(
            model_name='outletassignmentmodel',
            name='assignment_start',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 21, 2, 21, 36, 162839)),
        ),
    ]
