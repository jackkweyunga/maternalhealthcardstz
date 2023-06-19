from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms import HospitalRegistrationForm, UserRegistrationForm
from accounts.models import User


# Create your views here.

# stakeholders views
def stakeholders(request):
    return render(request, 'accounts/stakeholders.html')


# patient views
def login_patient(request, context):
    return render(request, 'accounts/login_patient.html', context)


# regulator views
def login_regulator(request, context):
    return render(request, 'accounts/login_regulator.html', context)


# researcher views
def login_researcher(request, context):
    return render(request, 'accounts/login_researcher.html', context)


# hospital views
def login_hospital(request, context):
    return render(request, 'accounts/hospital_login.html', context)


def custom_login(request):
    """
    An entrypoint view for login

    usage:

    patient login page => /accounts/login/?as=patient
    researcher login page => /accounts/login/?as=researcher
    regulator login page => /accounts/login/?as=regulator
    ... so on

    make a post request from any of these pages to login.

    checklist for the form in the template:
    - add `action` to the form in the specific template
    - add `method="post"`
    - add `{% csrf_token%}`
    - make sure the button is of type `submit`.

    """
    context = {}
    login_as = request.GET.get("as", None)

    print(login_as)

    # in case of a post request / login form submission.
    if request.method == "POST":
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        phone_number = request.POST.get("phone_number", None)
        hospital_id = request.POST.get("hospital_id", None)  # use it as username
        password = request.POST.get("password", None)

        user = None

        # Look for user in the database matching any of the passed credentials above.
        # if all checks fail the user remains `None` and redirected back to the login page.

        if email is not None:
            user = User.objects.filter(
                email=email
            ).first()
        elif username is not None:
            user = User.objects.filter(
                username=username
            ).first()
        elif phone_number is not None:
            user = User.objects.filter(
                phone_number=phone_number
            ).first()
        elif hospital_id is not None:
            user = User.objects.filter(
                username=hospital_id
            ).first()

        if password is None:
            context["errors"] = ["wrong login credentials"]

        elif user is not None and user.check_password(password):

            user: User = user

            # redirect to a specific page according to the user's role / permission

            # 1. check if is real a hospital login.
            if login_as == "hospital":

                is_hospital = False
                try:
                    print(user.hospital)
                    print(user.hospital is not None)
                    is_hospital = user.hospital is not None
                except Exception as e:
                    pass

                if is_hospital:
                    # login the user
                    login(request, user)
                    return redirect(reverse("regs:hospitaldash"))
                else:
                    context["errors"] = ["Wrong hospital credentials"]

            elif login_as == "regulator":
                # default redirect
                # login the user
                login(request, user)
                return redirect(reverse("regs:regulatordash"))

        else:

            context["errors"] = ["wrong login credentials"]

    # in case of a get request or login errors

    if login_as == "researcher":
        return login_researcher(request, context)
    elif login_as == "regulator":
        return login_regulator(request, context)
    elif login_as == "patient":
        return login_patient(request, context)
    elif login_as == "hospital":
        return login_hospital(request, context)
    else:
        return stakeholders(request)


def register_researcher(request):
    return render(request, 'accounts/register_researcher.html')


def register_hospital(request):
    context = {"errors": []}
    if request.method == "POST":
        data = request.POST.copy()

        print(data)

        password = data.pop("password1")[0]
        password2 = data.pop("password2")[0]

        email = data.get("email")
        hospital_id = data.get("hospital_id")
        phone_number = data.get("phone_number")

        print(email)

        user_ser = UserRegistrationForm(
            data={
                "email": email, "password": password, "password2": password2,
                "username": hospital_id, "phone_number": phone_number
            }
        )

        hospital_ser = HospitalRegistrationForm(data)
        if user_ser.is_valid():
            if hospital_ser.is_valid():
                user = user_ser.save()
                user.set_password(password)
                user.save()
                hospital = hospital_ser.save()
                hospital.user = user
                hospital.save()
                return redirect(reverse("accounts:login") + "?as=hospital")
            else:
                context["errors"].append(hospital_ser.errors)

        else:
            context["errors"].append(user_ser.errors)
    print(context)
    return render(request, 'accounts/hospital_register.html', context)


# forgot password
def forgot_password(request):
    return render(request, 'regs/forgot_password.html')
