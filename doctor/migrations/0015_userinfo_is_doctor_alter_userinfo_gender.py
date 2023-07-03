# Generated by Django 4.2.1 on 2023-07-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0014_remove_appointment_readings'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], max_length=50, null=True),
        ),
    ]
