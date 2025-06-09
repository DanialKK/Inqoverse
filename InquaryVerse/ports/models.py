from django.db import models

class Port(models.Model):
    name = models.CharField(max_length=255, verbose_name="نام بندر")
    country = models.CharField(max_length=255, verbose_name="کشور")
    code = models.CharField(max_length=10, unique=True, verbose_name="کد بندر (مثلاً UN/LOCODE)")

    def __str__(self):
        return f"{self.name} - {self.country}"
