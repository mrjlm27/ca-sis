# Generated by Django 2.2 on 2022-02-13 06:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0022_auto_20220212_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradereport',
            name='year_average',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_birthday',
            field=models.DateField(default=datetime.date(2022, 2, 13)),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_signdate',
            field=models.DateField(default=datetime.date(2022, 2, 13)),
        ),
    ]
