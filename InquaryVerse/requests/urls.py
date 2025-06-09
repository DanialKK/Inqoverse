from django.urls import path
from .views import InquiryRequestListCreateAPIView, AllInquiryRequestListAPIView

urlpatterns = [
    path('inquiries/', InquiryRequestListCreateAPIView.as_view(), name='inquiry-list-create'),
    path('', AllInquiryRequestListAPIView.as_view(), name='inquiry-list-view'),
]
