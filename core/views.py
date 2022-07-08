from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import StudentForm
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
    forms = StudentForm()
    context = {'forms':forms}
    return render(request,'studentform.html',context)            


def home(request):
    return render(request, 'home.html')
