from django.shortcuts import render

# Create your views here.

# stakeholders views
def stakeholders(request):
    return render(request, 'accounts/stakeholders.html')

# patient views
def login_patient(request):
    return render(request, 'accounts/login_patient.html')

# regulator views
def login_regulator(request):
    return render(request, 'accounts/login_regulator.html')

# researcher views
def login_researcher(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'accounts/login_researcher.html')

def register_researcher(request):
    return render(request, 'accounts/register_researcher.html')

# hospital views
def login_hospital(request):
    return render(request, 'accounts/hospital_login.html')

def register_hospital(request):
    return render(request, 'accounts/hospital_register.html')

# forgot password
def forgot_password(request):
    return render(request, 'regs/forgot_password.html')
