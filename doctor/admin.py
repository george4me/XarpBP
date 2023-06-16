from django.contrib import admin
from .models import Appointment, UserInfo, PatientReadings
# Register your models here.

admin.site.register(Appointment)


class UserInfoAdmin(admin.ModelAdmin):
    fields=['user', 'gender', 'phone']
admin.register(UserInfo, UserInfoAdmin)


class PatientReadingsAdmin(admin.ModelAdmin):
    fields=['user', 'bp_sys', 'bp_dia', 'bp_pulse', 'blood_sugar', 'datetime']    
admin.register(PatientReadings, PatientReadingsAdmin)
