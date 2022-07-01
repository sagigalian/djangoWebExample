from django.urls import path
from . import views

urlpatterns = [
	path("signup/", views.signup, name="signup"),
	path("login/", views.login, name="login"),
	path("myprofile/", views.myprofile, name="myprofile"),
	path("home/", views.home, name="home"),
	path("", views.home, name="home"),
	path("manager/", views.manager, name="manager"),
	path("users/", views.users, name="users"),
]