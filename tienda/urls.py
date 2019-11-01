from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('ventas/', include('ventas.urls')),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)