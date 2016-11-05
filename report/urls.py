from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<lang>[en, it, de]+)/$', views.ReportPage, name='Report'),
    url(r'^(?P<lang>[en, it, de]+)/reportForm$', views.ReportForm, name='ReportForm'),
    url(r'^(?P<lang>[en, it, de]+)/reportReceived$', views.getReport, name='getReport'),
    url(r'^(?P<lang>[en, it, de]+)/reportMody$', views.reportMody, name='ReportMody'),
    url(r'^(?P<lang>[en, it, de]+)/reportModified$', views.reportModified, name='ReportModified'),
    #url(r'^$', views.redirect, name='redirec')
]
