from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


def user_signup(request):
    return render(request, 'signup.html')


def user_login(request):
    fm = AuthenticationForm(request=request, data=request.POST)
    if fm.is_valid():
        username = fm.cleaned_data['username']
        password = fm.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully!!!')
            return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})


def student_form(request):
    return render(request,'studentform.html')
def home(request):
    return render(request,'home.html')
