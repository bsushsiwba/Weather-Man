from django.urls import path

from . import views

urlpatterns = [
    path("", views.login, name="index"),
    path("login/", views.login, name="register"),
    # path("login/", views.login, name="login"),
    # path("logout/", views.logout, name="logout"),
    # path("register/", views.register, name="register"),
    # path("change_password/", views.change_password, name="change_password"),
]
