from django.urls import path
from . import views

app_name = 'utility'
urlpatterns = [
    path('', views.index, name='index'),
]
