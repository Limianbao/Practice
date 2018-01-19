from django.conf.urls import url,include
from django.contrib import admin
import views
urlpatterns = [
    url('^first/$',views.first,name='first'),
    url('^registered/$',views.registered,name='registered'),
    url('^landing/$',views.landing,name='landing'),
    url('^query/$',views.query,name='query'),
    url('^success/$',views.success,name='success'),
    url('^deletes/$',views.deletes,name='deletes'),
]
