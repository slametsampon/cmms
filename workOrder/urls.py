from django.urls import path
from . import views

app_name = 'workOrder'
urlpatterns = [
    path('', views.index, name='index'),
    path('work_orders/', views.Work_orderListView.as_view(), name='work_orders'),
    path('work_order/<int:pk>', views.Work_orderDetailView.as_view(), name='work_order-detail'),
]

urlpatterns += [  
    path('work_order/create/', views.Work_orderCreate.as_view(), name='work_order-create'),
    path('work_order/<int:pk>/update/', views.Work_orderUpdate.as_view(), name='work_order_update'),
    path('work_order/<int:pk>/forward/', views.Work_orderForward.as_view(), name='work_order-forward'),
    path('work_order/<int:pk>/complete/', views.WoCompletion.as_view(), name='work_order-complete'),
]

urlpatterns += [  
    path('wo_instruction/<int:pk>/create/', views.Wo_instructionCreate.as_view(), name='wo_instruction-create'),
]

urlpatterns += [  
    path('work_order/summary/', views.WoSummaryReportView.as_view(), name='work_order-summary'),
    path('report/', views.WoReportView.as_view(), name='workOrder-report'),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
