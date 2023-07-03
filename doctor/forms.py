from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserInfo, PatientReadings
from django.forms import ModelForm



# class RegistrationForm(UserCreationForm):
#     first_name=forms.CharField(max_length=50, required=True)
#     last_name=forms.CharField(max_length=50, required=False)
#     #phone=forms.CharField(max_length=50, required=False)
#     #gender=forms.CharField(max_length=50, required=False)
#     username=forms.CharField(max_length=50, required=True)
#     email=forms.CharField(max_length=50)
#     password1=forms.CharField(max_length=50)
#     password2=forms.CharField(max_length=50)


#     class Meta:
#         model=User
#         fields=('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required. Enter a valid email address.')
    #user_type = forms.ChoiceField(choices=(('doctor', 'Doctor'), ('patient', 'Patient')), widget=forms.RadioSelect)
    gender = forms.ChoiceField(choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Prefer not to say')), widget=forms.RadioSelect)
    phone = forms.CharField(max_length=50, required=False)
    is_doctor = forms.BooleanField()
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'is_doctor', 'password1', 'password2', 'gender', 'phone')

    """
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user"""
    
class PatientReadingForm(ModelForm):
    bp_sys = forms.IntegerField(required=False)
    bp_dia= forms.IntegerField(required=False)
    bp_pulse = forms.IntegerField(required=False)
    blood_sugar = forms.IntegerField(required=False)
    datetime = forms.DateTimeField()

    class Meta:
        model=PatientReadings
        fields=('bp_sys', 'bp_dia', 'bp_pulse', 'blood_sugar', 'datetime', )
