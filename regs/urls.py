
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
    path("registeringpatient", views.registeringpatient, name="registeringpatient"),
    path("stakeholders", views.stakeholders, name="stakeholders"),
    path("loginhospital", views.loginhospital, name="loginhospital"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("researchdashboard", views.researchdashboard, name="researchdashboard"),
    path("researchdashpublications", views.researchdashpublications, name="researchdashpublications"),
    path("researchdashprofile", views.researchdashprofile, name="researchdashprofile"),
    path("regulatordash", views.regulatordash, name="regulatordash"),
    path("regulatordash_hospitals", views.regulatordash_hospitals, name="regulatordash_hospitals"),
    path("regulatordashprofile", views.regulatordashprofile, name="regulatordashprofile"),
    path("visualdata", views.regulatordash_visualdata, name="visualdata"),
    path("regulatordash_published", views.regulatordash_published, name="regulatordash_published"),
    path("regulatordash_reports", views.regulatordash_reports, name="regulatordash_reports"),

]

