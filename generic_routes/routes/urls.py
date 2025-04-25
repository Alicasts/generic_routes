from django.urls import path
from .views import DynamicViewNoParam, DynamicViewWithParam

urlpatterns = [
    path('', DynamicViewNoParam.as_view(), name='dynamicRoot'),
    path('<str:routeParameter>/', DynamicViewWithParam.as_view(), name='dynamicHandling'),
]