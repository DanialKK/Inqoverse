from rest_framework import generics
from .models import Port
from .serializers import PortSerializer

class PortListAPIView(generics.ListAPIView):
    queryset = Port.objects.all()
    serializer_class = PortSerializer
