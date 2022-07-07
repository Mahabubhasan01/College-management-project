from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')
def user_signup(request):
    return render(request,'signup.html')
def user_login(request):
    return render(request,'login.html')