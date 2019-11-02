from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^contacts/$', views.contacts, name = 'contacts'),
url(r'^upload/$', views.upload, name = 'upload')
]
