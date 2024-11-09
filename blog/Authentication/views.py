from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
