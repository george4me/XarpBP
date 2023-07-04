from django.db import models
from django.http import request
from django.contrib.auth.models import User



class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]


class UserInfo(models.Model):
    GENDER_CHOICE=(
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Prefer not to say')
    )
    user=models.OneToOneField(User, related_name='user_info', on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICE, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    is_doctor = models.BooleanField()


    def __str__(self):
        return "%s" % self.user.username
    

class PatientReadings(models.Model):
    user=models.ForeignKey(User, related_name='patient', on_delete=models.CASCADE)
    bp_sys = models.IntegerField(null=True, blank=True)
    bp_dia= models.IntegerField(null=True, blank=True)
    bp_pulse = models.IntegerField(null=True, blank=True)
    blood_sugar = models.IntegerField(null=True, blank=True)
    datetime = models.DateTimeField()

    



class Videos(models.Model):
    caption=models.CharField(max_length=100)
    videos=models.FileField(upload_to="video/%y")
    def __str__(self):
        return self.caption   