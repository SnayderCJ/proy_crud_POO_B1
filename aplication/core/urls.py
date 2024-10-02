from django.urls import path
from aplication.core import views

urlpatterns = [
    path('doctor/', views.doctor_List , name='doctor_list'),
    path('doctor_create/', views.doctor_create,name="doctor_create"),
]
