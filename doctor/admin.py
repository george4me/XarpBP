from django.contrib import admin
from .models import Appointment, UserInfo, PatientReadings, Videos
# Register your models here.

admin.site.register(Appointment)

admin.site.register(Videos)


class UserInfoAdmin(admin.ModelAdmin):
    fields=['user', 'gender', 'phone']


admin.register(UserInfo, UserInfoAdmin)



@admin.register(PatientReadings)
class PatientReadingsAdmin(admin.ModelAdmin):
    list_display = ['user','bp_sys', 'bp_dia']
