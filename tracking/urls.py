from django.conf.urls import url

from . import views
from . import json_view
from . import file_parser

urlpatterns = [

    url(r'^$', views.upload_file),
    url(r'^track-(?P<track_id>[a-zA-Z0-9]{1,})$', json_view.print_json, name="print_json"),	
    url(r'^success/url$', views.success, name='success'),
    url(r'^trackload-(?P<track_file>[a-zA-Z0-9]{1,})$', file_parser.load_gpx),	 
]
