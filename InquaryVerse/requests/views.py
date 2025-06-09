from rest_framework import generics, permissions
from .models import InquiryRequest
from .serializers import InquiryRequestSerializer

class InquiryRequestListCreateAPIView(generics.ListCreateAPIView):
    queryset = InquiryRequest.objects.all()
    serializer_class = InquiryRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AllInquiryRequestListAPIView(generics.ListAPIView):
    queryset = InquiryRequest.objects.all().order_by('-created_at')
    serializer_class = InquiryRequestSerializer
      # یا IsAdminUser اگر فقط ادمین بخواد ببینه
