from django.urls import path
from . import views

app_name = 'help'
urlpatterns = [
    path('', views.cmms, name='cmms'),
    path('workOrder/', views.workOrder, name='workOrder-Help'),
    path('PmPdm/', views.PmPdm, name='PmPdm-Help'),
    path('Equipment/', views.Equipment, name='Equipment-Help'),
    path('Utility/', views.Utility, name='Utility-Help'),
    path('Reporting/', views.Reporting, name='Reporting-Help'),
]
