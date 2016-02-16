from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^(?P<appId>[0-9]+)/$', views.edit, name='edit'),
	url(r'^upload/$', views.upload, name='upload'),
]