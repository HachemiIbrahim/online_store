from django.contrib.auth import views as auth_views
from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("contact/", views.contact, name="contact"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView, name="login"),
]
