from django.urls import path
from .views import handleRequest

urlpatterns = [
    path('', handleRequest, name='dynamicRoot'),
    path('<str:routeParameter>/', handleRequest, name='dynamicGet'),
]