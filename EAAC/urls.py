from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',
    url(r'',            include('website.urls', namespace='website')),
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^timetable/', include('timetable.urls', namespace='timetable')),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^instructors/', include('instructors.urls', namespace='instructors')),
    (r'^accounts/', include('allauth.urls')),
    url (r'^accounts/profile/', include('accounts.urls', namespace='profile')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
