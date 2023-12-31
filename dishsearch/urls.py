from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("", include("dish.urls")),
    path("admin/", admin.site.urls),
    path("user/", include("user.urls")),
    path("restaurant/", include("restaurant.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
