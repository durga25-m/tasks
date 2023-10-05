from django.shortcuts import render, redirect
#from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth
from django.contrib import messages

def loginView(request):
    return render(request, 'login.html')

def signupView(request):
    return render(request,'signup.html')

def taskView(request):
    return render(request,'task.html')