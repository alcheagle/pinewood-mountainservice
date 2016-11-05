from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^homepage/(?P<lang>[en, it, de]+)/$', views.IndexPage, name='Index'),
    #url(r'^$', views.redirect, name='redirec')
]
