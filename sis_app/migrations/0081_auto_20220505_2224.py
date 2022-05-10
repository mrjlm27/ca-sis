# Generated by Django 3.0.2 on 2022-05-05 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0080_gradereport_gradelevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paymentdate_date',
            field=models.DateField(default=datetime.date(2022, 5, 5)),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_birthday',
            field=models.DateField(default=datetime.date(2022, 5, 5)),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_schoolyear_start',
            field=models.IntegerField(choices=[(2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026)], default=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_signdate',
            field=models.DateField(default=datetime.date(2022, 5, 5)),
        ),
    ]