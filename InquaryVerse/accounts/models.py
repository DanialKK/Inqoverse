from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_company = models.BooleanField(default=False, verbose_name="شرکت هست؟")
    national_id = models.CharField(max_length=10, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    economic_code = models.CharField(max_length=20, blank=True, null=True)
    registration_number = models.CharField(max_length=20, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.username
