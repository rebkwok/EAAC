from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField('instructor description', blank=True, null=True)
    photo = models.ImageField(upload_to='instructors', null=True, blank=True, help_text="Please upload a .jpg image with equal height and width")

    def __unicode__(self):
        return self.name

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
            this = Instructor.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except: pass # when new photo then we do nothing, normal case
        super(Instructor, self).save(*args, **kwargs)
