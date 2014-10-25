from django.contrib import admin
from instructors.models import Instructor


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_photo')

admin.site.register(Instructor, InstructorAdmin)
