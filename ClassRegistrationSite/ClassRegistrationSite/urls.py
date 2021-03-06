"""ClassRegistrationSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = "default"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.redirect_login, name='blank'),
    path('login/', views.userlogin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('landingpage/', views.landingpage, name='landingpage'),
    path('register/', views.register_classes, name="register"),   #show all classes, based on class ID
    path('show_schedule/', views.show_schedule, name="show_schedule"),  #show registered classes
    path('<slug:err>/', views.err, name="err"),

]
