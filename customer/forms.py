from django import forms
from django.core import validators
from django.contrib.auth.models import User
from .models import Customer
from bootstrap_datepicker_plus import DatePickerInput
class SignupForm(forms.ModelForm):
    def clean(self):
        cl_data=super().clean()
        passw1=cl_data.get('password1')
        passw2=cl_data.get('password2')
        if len(passw1)<9 or passw1.isnumeric():
            raise forms.ValidationError('*The password should be longer then 8 char. \t*the password should not contain only numbers')
        if passw1!=passw2:
            raise forms.ValidationError('Passwords don\'t match')
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Repeat Password',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password1','password2','email','first_name','last_name',]
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        exclude=['user']
        widgets = {
            'birth_date': DatePickerInput(), # default date-format %m/%d/%Y will be used

        }
