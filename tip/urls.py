from django.contrib import admin
from django.urls import path
from tip import views

urlpatterns = [
    path('', views.tips, name="tips"),
    path('cosmetics/<int:id>', views.cosmetics, name="cosmetics"),
    path('create/', views.create, name="create"),
]