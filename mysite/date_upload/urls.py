from django.conf.urls import url
from date_upload import views

app_name = 'data_upload'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]