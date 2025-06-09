from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from django.views.generic import TemplateView

urlpatterns = [
    # API endpoints
    path('register-api/', RegisterView.as_view(), name='register_api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # صفحات HTML
    path('login/', TemplateView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='accounts/register.html'), name='register'),
]
