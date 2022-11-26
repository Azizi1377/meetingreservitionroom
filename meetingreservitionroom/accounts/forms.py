from django import forms
from django.contrib.auth.models import User



class UserRegisterationForm(forms.Form):
    username = forms.CharField(label="نام کاربری")
    email = forms.EmailField(label="ایمیل")
    password = forms.CharField(widget=forms.PasswordInput(), label="کلمه عبور")
    first_name = forms.CharField(label="نام")
    last_name = forms.CharField(label="نام خانوادگی")
    class Meta:
        model = User


class UserLoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput(), label="کلمه عبور")
    class Meta:
        model = User
       