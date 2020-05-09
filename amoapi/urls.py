from django.urls import path
from . import views

urlpatterns = [
    path('send_email', views.send_email),
    path('leads/', views.leads),
    path('paints/', views.paints)
]