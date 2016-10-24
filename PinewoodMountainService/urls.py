"""PinewoodMountainService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def mainPage (request):
    template=loader.get_template('main/mainPage.html')
#    return HttpResponse ('ciao')
    return HttpResponse (template.render(request))

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainPage),
#    url(r'^', views.MainPageView.as_view()),
#    url(r'^index/', views.MainPageView.as_view()),
    url(r'^tracking/', include('tracking.urls')),
    url(r'^hook/', include('autodeploy.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
