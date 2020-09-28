from django.urls import path
from . import views

app_name = 'reporting'
urlpatterns = [
    path('', views.ReportingHomeView.as_view(), name='index'),
]
