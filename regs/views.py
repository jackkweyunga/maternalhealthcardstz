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

def registeringpatient(request):
    return render(request, 'regs/dash_register_patient.html')

def stakeholders(request):
    return render(request, 'regs/stakeholders.html')

def loginhospital(request):
    return render(request, 'regs/hospital_login.html')

def dashboard(request):
    return render(request, 'regs/dashboard.html')

def researchdashboard(request):
    return render(request, 'regs/researchdash.html')

def researchdashpublications(request):
    return render(request, 'regs/researchdash_publications.html')

def researchdashprofile(request):
    return render(request, 'regs/researchdash_profile.html')

def regulatordash(request):
    return render(request, 'regs/regulatordash.html')

def regulatordash_hospitals(request):
    return render(request, 'regs/regulatordash_hospitals.html')

def regulatordashprofile(request):
    return render(request, 'regs/regulatordashprofile.html')

def regulatordash_visualdata(request):
    return render(request, 'regs/regulatordash_visualdata.html')

def regulatordash_published(request):
    return render(request, 'regs/regulatordash_published.html')

def regulatordash_reports(request):
    return render(request, 'regs/regulatordash_reports.html')

def loader(request):
    return render(request, 'regs/loader.html')

# classical views with classes
# from django.views import generic