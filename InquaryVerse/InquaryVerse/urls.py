from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('api/ports/', include('ports.urls')),
    path('api/requests/', include('requests.urls')),
    path('auth/', include('accounts.urls')),
    path('api/accounts/', include('accounts.urls')),
]

