from django.urls import path
from .views import PortListAPIView

urlpatterns = [
    path('', PortListAPIView.as_view(), name='port-list'),
]
