from django.shortcuts import render, redirect
from .forms import UserRegisterationForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



def user_register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            if User.objects.filter(username = cd['username']).first():
                messages.error(request, "نام کاربری پیش از این انتخاب شده است")
                return redirect('user_register')
            
            if User.objects.filter(email = cd['email']).first():
                messages.error(request, "ایمیل پیش از این انتخاب شده است")
                return redirect('user_register')
            
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            
            messages.success(request, 'ثبت نام کاربر با موفقیت انجام شد', 'success')
            return redirect('statusroom')
    else:
        form = UserRegisterationForm()
    return render(request, 'register.html', {'form':form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user= authenticate(request, username=cd['username'], password=cd['password'])
    
            if user is not None:
                login(request, user)
                messages.success(request, 'ورود کاربر با موفقیت انجام شد', 'success')
                return redirect('statusroom')      
            elif user is None:
                messages.error(request, 'نام کاربری یا رمز ورود نامعتبر', 'danger')
                return redirect('user_login')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form':form})
    

def user_logout(request):
    logout(request)
    messages.success(request, 'خروج کاربر با موفقیت انجام شد', 'success')
    return redirect('user_login')