from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('balitassap.urls')),
]
urlpatterns += static(settings.MEDIA_URL, serve, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, serve, document_root=settings.STATIC_ROOT)










