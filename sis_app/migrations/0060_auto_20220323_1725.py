# Generated by Django 2.2 on 2022-03-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0059_auto_20220323_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gradereport',
            name='gradelevel',
            field=models.CharField(blank=True, choices=[('Nursery', 'Nursery'), ('Kinder 1', 'Kinder 1'), ('Kinder 2 Junior', 'Kinder 2 Junior'), ('Kinder 2 Senior', 'Kinder 2 Senior')], default=None, max_length=30),
        ),
    ]
