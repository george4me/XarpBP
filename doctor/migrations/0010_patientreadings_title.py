# Generated by Django 4.2.1 on 2023-06-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0009_appointment_readings'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientreadings',
            name='title',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]