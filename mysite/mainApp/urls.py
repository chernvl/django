from django.conf.urls import url
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^news/$', views.news, name = 'news'),
    url(r'^contacts/$', views.contacts, name = 'contacts')
]
