from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r"^admin/filebrowser/", include("filebrowser_safe.urls")),
    url(r"^admin/", admin.site.urls),
]
