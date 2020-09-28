from django.urls import path
from . import views

app_name = 'help'
urlpatterns = [
    path('', views.HelpHomeView.as_view(), name='cmms'),
    path('workOrder/', views.HelpWorkOrderView.as_view(), name='workOrder-Help'),
    path('PmPdm/', views.HelpPmPdmView.as_view(), name='PmPdm-Help'),
    path('Equipment/', views.HelpEquipmentView.as_view(), name='Equipment-Help'),
    path('Utility/', views.HelpUtilityView.as_view(), name='Utility-Help'),
    path('Reporting/', views.HelpReportingView.as_view(), name='Reporting-Help'),
]
