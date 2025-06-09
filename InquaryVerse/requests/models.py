from django.db import models
from django.conf import settings
from ports.models import Port

CONTAINER_TYPE_CHOICES = [
    ('20', '۲۰ فوت'),
    ('40', '۴۰ فوت'),
]

class InquiryRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="کاربر")
    product_type = models.CharField(max_length=255, verbose_name="نوع کالا")
    container_type = models.CharField(max_length=2, choices=CONTAINER_TYPE_CHOICES, verbose_name="نوع کانتینر")
    container_count = models.PositiveIntegerField(verbose_name="تعداد کانتینر")
    origin = models.ForeignKey(Port, on_delete=models.SET_NULL, null=True, related_name='origin_requests', verbose_name="مبدأ")
    all_ports = models.BooleanField(default=False, verbose_name="همه بنادر؟")
    destination = models.CharField(max_length=255, verbose_name="مقصد")
    target_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="قیمت پیشنهادی", null=True, blank=True)
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return f"درخواست {self.user} برای {self.product_type}"
