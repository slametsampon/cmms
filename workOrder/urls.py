from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('work_orders/', views.Work_orderListView.as_view(), name='work_orders'),
    path('work_order/<int:pk>', views.Work_orderDetailView.as_view(), name='work_order-detail'),
]

urlpatterns += [  
    path('work_order/create/', views.Work_orderCreate.as_view(), name='work_order_create'),
    path('work_order/<int:pk>/update/', views.Work_orderUpdate.as_view(), name='work_order_update'),
]

urlpatterns += [  
    path('user_profile_update/', views.ProfileUpdateView.as_view(), name='user_profile_update'),
]