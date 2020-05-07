from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register),
    path('reset_pass_mail/', views.reset_pass_mail),
    path('reset_pass/', views.reset_pass),
    path('entry/test/', views.test),
]
