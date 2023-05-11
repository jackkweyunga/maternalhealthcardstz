from django.urls import path

from . import views

# namespacing urls for easier url referencing
app_name = "regs"

urlpatterns = [ 
    path("", views.index, name="home"),
    path("research", views.research, name="research"),
    path("patient", views.patient, name="patient"),
    path("regulator", views.regulator, name="regulator"),
    path("hospital", views.hospital, name="hospital"),
    path("forgotpassword", views.forgotpassword, name="forgotpassword"),
    path("loginresearcher", views.loginresearcher, name="loginresearcher"),

]

