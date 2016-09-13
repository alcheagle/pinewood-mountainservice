from django.conf.urls import url

from . import views
from . import json_view

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.UploadView.as_view()),	
    url(r'^track-(?P<track_id>)$/', json_view.print_json),	
]
