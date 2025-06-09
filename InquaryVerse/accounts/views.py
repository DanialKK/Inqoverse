from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import RegisterSerializer
from django.views.generic import TemplateView

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class RegisterTemplateView(TemplateView):
    template_name = 'accounts/register.html'

class LoginTemplateView(TemplateView):
    template_name = 'accounts/login.html'

