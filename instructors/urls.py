from django.conf.urls import patterns, url

urlpatterns = patterns(
    'instructors.views',
    url(r'^(?P<instructor_id>\d+)/instructor/$', 'instructor_info', name='instructor_info'),
    url(r'^instructors$',       'instructors', name='instructors'),
    )