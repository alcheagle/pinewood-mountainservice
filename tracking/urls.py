from django.conf.urls import url

from . import views
from . import json_view

urlpatterns = [

    url(r'^$', views.upload_file),	
    url(r'^track-(?P<track_id>[0-9]{1,8})$', json_view.print_json, name="print_json"),	
    url(r'^success/url$', views.success, name='success'),
]
