from django.conf.urls import patterns, url

urlpatterns = patterns(
    'timetable.views',
    url(r'^timetable$',         'timetable', name='timetable'),
    )
