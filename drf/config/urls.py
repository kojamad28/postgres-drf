from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from config.settings.development import env
#from config.settings.production import env

urlpatterns = [
    path("api/accounts/", include("accounts.urls")),
    path(env("ADMIN_URL", default="admin/"), admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += [path(env("SILK_URL", default="silk/"), include("silk.urls", namespace="silk"))]
