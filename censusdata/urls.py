from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from member.views import memadd, status, visualise, censusvisual


urlpatterns = [
    url(r'^$', visualise),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^memberadd/', memadd),
    url(r'^memlist/', status),
    url(r'^censusvisual', censusvisual),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
