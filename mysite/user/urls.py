from django.conf.urls import url
from . import views
app_name = 'user'
urlpatterns = [
    url(r'^form/$', views.form, name= 'form'),
    url(r'^test/$', views.test, name= 'test'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^plo/$', views.plo, name= 'plo'),
]