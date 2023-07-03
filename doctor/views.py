from typing import Any, Dict
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Appointment, PatientReadings, Videos
from django.views.generic import ListView
import datetime
from django.template import Context
from django.template.response import TemplateResponse
from django.template.loader import render_to_string, get_template
from django.contrib.auth import logout, login, authenticate
from .forms import RegistrationForm, PatientReadingForm
from django.shortcuts import redirect
from .models import UserInfo


class HomeTemplateView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        email = EmailMessage(
            subject= f"{name} from doctor family.",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        return HttpResponse("Email sent successfully")


class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html" 
    model = Appointment
    context_object_name = "appointments"
    login_required = True 
    paginate_by = 3  


    def post(self, request):
        date = request.POST.get("date")
        appointments_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointments_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of{appointment.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title":"Manage Appointments"
        })
        return context
    #end def get_context_data
#end class



class ManageReadingsTemplateView(ListView):
    template_name = "manage-readings.html" 
    model = PatientReadings
    context_object_name = "patients_readngs"
    login_required = True 
    paginate_by = 3  

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = PatientReadings.objects.all()
        context.update({
            "title":"Manage Readings"
        })
        return context
    #end def get_context_data
#end class


def Logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def registeration_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
        if form.cleaned_data["user_type"] == "doctor":
            user.is_staff = True
            user_type = form.cleaned_data['user_type']
            #UserType.objects.create(user=user, type=user_type)
            UserInfo.objects.create(user=user, phone=form.cleaned_data['phone'], gender=form.changed_data['gender'])
            return redirect('login') 
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form}) 
    # form=RegistrationForm(request.POST)
    # if request.method=='POST':
    #     if form.is_valid():
    #         first_name=form.cleaned_data['first_name']
    #         last_name=form.cleaned_data['last_name']
    #         username=form.cleaned_data['username']
    #         email=form.cleaned_data['email']
    #         password1=form.cleaned_data['password1']
    #         password2=form.cleaned_data['password2']
    #         if password1 != password2:
    #             return render(request, 'register.html')
    #         else:
    #             newuser=form.save()
    #             newuser.save()

    #             phone=request.POST['phone']
    #             gender=request.POST['gender']

    #             userinfo = UserInfo(
    #                 user_id = newuser.id,
    #                 gender = gender,
    #                 phone=phone
    #             )
    #             userinfo.save()

    #             return redirect('login')


    # return render(request, 'register.html')



def doctor_registeration_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    form=RegistrationForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            if password1 != password2:
                return render(request, 'register.html')
            else:
                newuser=form.save()
                newuser.save()

                newuser.is_staff = True
                newuser.save()

                phone=request.POST['phone']
                gender=request.POST['gender']

                userinfo = UserInfo(
                    user_id = newuser.id,
                    gender = gender,
                    phone=phone
                )
                userinfo.save()

                return redirect('login')


    return render(request, 'register.html')



def login_view(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, 'Login successful')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Login Error!!! Username or PAssword incorect')

    return render(request, 'login.html')


def submit_readings(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('login/')
     
    if not request.method == 'POST':
        return HttpResponse(status=400)
    
    user = request.user
    bp_sys = request.POST['bp_sys']
    bp_dia = request.POST['bp_dia']
    bp_pulse = request.POST['bp_pulse']
    blood_sugar = request.POST['blood_sugar']
    datetime = request.POST['datetime']

    create_reading = PatientReadings.objects.create(user=user, bp_sys=bp_sys, bp_dia=bp_dia, bp_pulse=bp_pulse, blood_sugar=blood_sugar, datetime=datetime)

    return TemplateResponse(request, 'submit_readings.html', {"create_reading":create_reading, "response":"readings submitted"})


def get_readings(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect('login/')

    if not request.method == 'GET':
        return HttpResponse(status=400)
        
    if 'user_id' not in request.query_params:
        return HttpResponse('user_id not provided', status=400)
    readings=PatientReadings.objects.filter(user_id=request.query_params['user_id'])

    all_readings = {}
    for reading in readings:
        all_readings[reading.id] = {
        "bp_sys": reading.bp_sys,
        "bp_dia": reading.bp_dia,
        "bp_pulse": reading.bp_pulse,
        "blood_sugar": reading.blood_sugar,
        "datetime": reading.datetime
    }

    return TemplateResponse(request, 'login.html', {"all_readings":all_readings, "fn_user":request.user.first_name, "ln_user":request.user.last_name})


def video_view(request):
    if request.method == 'POST':
        caption = request.POST['caption']
        video_file = request.FILES['video_file']
        video = Videos(caption=caption, videos=video_file)
        video.save()
        return redirect('videos')
    else:
        videos = Videos.objects.all()
        return render(request, 'videos.html', {'videos': videos})

def patient_readings_view(request):


    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        form = PatientReadingForm(request.POST)
        if form.is_valid():
            bp_sys = request.POST.get('bp_sys') # form.cleaned_data['bp_sys'] 
            bp_dia = request.POST.get('bp_dia')
            bp_pulse = request.POST.get('bp_pulse')
            datetime = request.POST.get('datetime')
            blood_sugar = request.POST.get('blood_sugar')
            user = request.user

            # create the patientReadng instance
            data = PatientReadings()
            data.bp_sys = form.cleaned_data['bp_sys'] # you can also get the data this way
            data.bp_dia = bp_dia
            data.blood_sugar = blood_sugar
            data.bp_pulse = bp_pulse
            data.user = user
            data.datetime = datetime

            data.save()

            # send a message to the client or user
            messages.success(request, f"Dear {user} Your readings was successfully submitted.")

            # you can add much more things here like sending emails or ...
            return render(request, 'patient_readings.html')


    return render(request, 'patient_readings.html')
