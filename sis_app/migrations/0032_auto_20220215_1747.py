# Generated by Django 3.0.2 on 2022-02-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0031_auto_20220215_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradereport',
            name='school_year',
            field=models.IntegerField(default=None),
        ),
    ]
