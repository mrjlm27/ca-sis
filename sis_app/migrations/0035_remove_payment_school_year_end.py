# Generated by Django 3.0.2 on 2022-02-15 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0034_payment_school_year_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='school_year_end',
        ),
    ]
