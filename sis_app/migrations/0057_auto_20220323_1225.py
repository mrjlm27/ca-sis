# Generated by Django 3.0.2 on 2022-03-23 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0056_toggle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='paymentdate_date',
            field=models.DateField(default=datetime.date(2022, 3, 23)),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_birthday',
            field=models.DateField(default=datetime.date(2022, 3, 23)),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_signdate',
            field=models.DateField(default=datetime.date(2022, 3, 23)),
        ),
    ]