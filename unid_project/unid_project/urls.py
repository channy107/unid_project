from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('unid/', include('unid.urls')),
    url(r'^accounts/', include('allauth.urls')),
    # static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
]
