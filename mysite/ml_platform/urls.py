"""ml_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from date_upload import views
from django.conf.urls import url, include
from django.conf import settings
from  django.conf.urls.static import static

urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^admin/',admin.site.urls),
    url(r'^date_upload/',include('date_upload.urls')),
    url (r'^formpage/',views.form_name,name='form_name'),
    url (r'^models/models_list/',views.models_data,name='models_data'),
    url (r'^models/model_upload/',views.models_data_upload,name='model_upload'),
    url (r'logout/$',views.user_logout,name='logout'),
    url (r'special/',views.special,name='special'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)