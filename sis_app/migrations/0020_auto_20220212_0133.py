# Generated by Django 2.2 on 2022-02-11 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0019_auto_20220211_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_birthday',
            field=models.DateField(default=datetime.date(2022, 2, 12)),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_signdate',
            field=models.DateField(default=datetime.date(2022, 2, 12)),
        ),
    ]
