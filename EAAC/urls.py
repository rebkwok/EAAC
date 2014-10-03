from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    #url(r'^$', 'website.views.home', name='home'),
    #url(r'^timetable$', 'timetable.views', name='timetable'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
)
