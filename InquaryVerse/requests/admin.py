from django.contrib import admin
from .models import InquiryRequest

@admin.register(InquiryRequest)
class InquiryRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_type', 'container_type', 'container_count', 'origin', 'all_ports', 'destination', 'target_price', 'created_at')
    list_filter = ('container_type', 'all_ports', 'created_at')
    search_fields = ('product_type', 'destination', 'user__username')
