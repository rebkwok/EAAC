from django.conf.urls import patterns, url

urlpatterns = patterns(
    'gallery.views',
    url(r'^gallery',         'gallery', name='gallery'),
)
