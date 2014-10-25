from django.db import models
from instructors.models import Instructor
from timetable.choices import SESSION_TYPE_CHOICES

CLASS = SESSION_TYPE_CHOICES[0][0]


class Discipline(models.Model):
    """
    Discipline (e.g. trapeze, silks)
    """
    name = models.CharField(max_length=255)
    info = models.TextField('session description',  null=True)
    photo = models.ImageField(upload_to='sessions', null=True, blank=True)

    def has_photo(self):
        if self.photo:
            return True
        else:
            return False
    has_photo.short_description = 'Photo uploaded'
    has_photo.boolean = True

    def save(self, *args, **kwargs):
        # delete old image file when replacing by updating the file
        try:
            this = Discipline.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except:
            pass # when new photo then we do nothing, normal case
        super(Discipline, self).save(*args, **kwargs)


class Location(models.Model):
    """
    Session location; can be "all" for sessions such as Registration and breaks
    """
    room = models.CharField(max_length=255)
    area = models.CharField(max_length=255)



class Session(models.Model):
    """
    Timetabled session, used to manage individual classes and other timetabled sessions
    """
    level = models.CharField(max_length=255, default="All levels")
    session_date = models.DateTimeField('session date')
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    instructor = models.ForeignKey(Instructor, null=True, blank=True)
    discipline = models.ForeignKey(Discipline)
    session_type = models.CharField(max_length=12, choices=SESSION_TYPE_CHOICES, default=CLASS)
    location = models.ForeignKey(Location)
    spaces = models.BooleanField('spaces available', default=True)

    def set_booking(self):
        if self.session_type is not CLASS:
            self.spaces = False






