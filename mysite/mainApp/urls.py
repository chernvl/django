rom django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('mainApp.urls')),
    url(r'^webexample/', include('webexample.urls'))
]
if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
