# Generated by Django 2.2 on 2022-01-26 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sis_app', '0007_auto_20220126_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_enrollment_plan',
            field=models.CharField(choices=[('Annually', 'Annually'), ('Bi-Annually', 'Bi-Annually'), ('Quarterly', 'Quarterly')], default='Annually', max_length=20),
        ),
    ]