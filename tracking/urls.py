from django.conf.urls import url

from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
]
=======
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.UploadView.as_view()),	
]
>>>>>>> dd497379172b25363fcda92466d4be67315686e9
