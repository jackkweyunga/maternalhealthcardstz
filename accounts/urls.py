
from django.urls import path

from . import views


# namespacing urls for easier url referencing
app_name = "accounts"

urlpatterns = [

    # login page url
    path("login", views.custom_login, name="login"),

    path("register_hospital", views.register_hospital, name="register_hospital"),
    path("register_researcher", views.register_researcher, name="register_researcher"),

    path("forgot_password", views.forgot_password, name="forgot_password"),

 ]