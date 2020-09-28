"""thiscamp URL Configuration

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
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('add_my_soldier/<int:civil_id>/<int:soldier_id>/',views.add_my_soldier, name='add_my_soldier'),

    path('signup_select/', views.signup_select, name='signup_select'),
    path('soldier_signup/', views.soldier_signup, name='soldier_signup'),
    path('civil_signup/', views.civil_signup, name='civil_signup'),
    path('login/', views.login, name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]
