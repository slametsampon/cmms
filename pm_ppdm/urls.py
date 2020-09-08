from django.urls import path
from . import views

app_name = 'pm_ppdm'
urlpatterns = [
    path('', views.index, name='index'),
]
