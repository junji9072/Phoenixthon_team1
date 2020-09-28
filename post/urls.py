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
from django.urls import path,include
from . import views #post.views

urlpatterns = [
    path("notice/", views.notice_list, name="notice_list"),
    path("notice/detail/<int:post_id>/", views.notice_detail, name="notice_detail"),
    path("notice/create/", views.notice_create, name="notice_create"),
    path("notice/update/<int:post_id>/", views.notice_update, name="notice_update"),
    path("notice/delete/<int:post_id>/", views.notice_delete, name="notice_delete"),

    path("question", views.question_list, name="question_list"),
    path("question/create/", views.question_create, name="question_create"),
    path("question/detail/<int:post_id>/", views.question_detail, name="question_detail"),
    path("question/update/<int:post_id>/", views.question_update, name="question_update"),
    path("question/delete/<int:post_id>/", views.question_delete, name="question_delete"),

    path("answer/create/<int:question_id>/", views.answer_create, name="answer_create"),
    path("answer/update/<int:question_id>/<int:answer_id>/", views.answer_update, name="answer_update"),
    path("answer/delete/<int:question_id>/<int:answer_id>/", views.answer_delete, name="answer_delete"),
]
