
from django.urls import path
#from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView
#from . import views
from .views import *

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("manage-readings/", ManageReadingsTemplateView.as_view(), name="manage-readings"),
    #path('login/', views.login_view, name='login_view'),
    #path('register', views.register, name='register'),
    path('user_logout/', Logout_view, name="logout"),
    path('register/', registeration_view, name="register"),
    path('doctor-registration/', doctor_registeration_view, name="doctor-registration"),
    path('login/', login_view, name="login"),
    path('submit_readings/', patient_readings_view, name="patient-readings"),
    path('get_readings/', get_readings, name="get_readings"),
    path('videos/', video_view, name="videos"),
    
]
