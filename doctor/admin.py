from django.contrib import admin
from .models import Appointment, UserInfo, PatientReadings, Videos
# Register your models here.

admin.site.register(Appointment)

admin.site.register(Videos)


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    fields=['user', 'gender', 'phone']




@admin.register(PatientReadings)
class PatientReadingsAdmin(admin.ModelAdmin):
    list_display = ['user','bp_sys', 'bp_dia']
