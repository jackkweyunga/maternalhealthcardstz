from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'regs/index.html')

def research(request):
    return render(request, 'regs/register_researcher.html')

def patient(request):
    return render(request, 'regs/login_patient.html')

def regulator(request):
    return render(request, 'regs/login_regulator.html')

def hospital(request):
    return render(request, 'regs/hospital_register.html')

def forgotpassword(request):
    return render(request, 'regs/forgot_password.html')

def loginresearcher(request):
    return render(request, 'regs/login_researcher.html')

# classical views with classes
# from django.views import generic