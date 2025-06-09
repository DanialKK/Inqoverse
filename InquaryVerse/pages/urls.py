from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, InquiryCreateView, InquiryListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('inquiry/new/', InquiryCreateView.as_view(), name='inquiry_create'),
    path('inquiry/view/', InquiryListView.as_view(), name='inquiry_view'),

]
