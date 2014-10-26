from django.conf.urls import patterns, url

urlpatterns = patterns(
    'gallery.views',
    url(r'^$',         'gallery', name='gallery'),
    url(r'^(?P<category_id>\d+)/category/$', 'gallery_category', name='gallery_category'),
)
