# Generated by Django 4.2.1 on 2023-06-27 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_patientreadingresult'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientReadingResult',
        ),
    ]
