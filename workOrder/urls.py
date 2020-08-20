from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work_orders/', views.Work_orderListView.as_view(), name='work_orders'),
    path('work_order/<int:pk>', views.Work_orderDetailView.as_view(), name='work_order-detail'),
]
