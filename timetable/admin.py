from django.contrib import admin
from timetable.models import Session, Discipline, Location


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_photo')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('room', 'area')


class SessionAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'level', 'instructor', 'session_date', 'start_time', 'end_time', 'location',
                    'session_type', 'spaces', )
    fieldsets = [
        ('Session information', {'fields': ['discipline', 'level', 'instructor', 'location', 'session_type', 'spaces']}),
        ('Date and time',        {'fields': ['session_date', 'start_time', 'end_time']}),
         ]
    ordering = ['session_date']
    date_hierarchy = 'session_date'
    save_as = True



admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Location, LocationAdmin)