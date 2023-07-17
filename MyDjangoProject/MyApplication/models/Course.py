from django.db import models
from . import Organization
import uuid

class Course(models.Models):
    course_id = models.CharField(unique=True, null=True, blank=True, max_length=25)
    organization_id = models.ForeignKey(Organization, related_name='organization_id', tofield = 'organization_id')
    course_name = models.CharField(null=False, blank=False, max_length=155)
    course_status = models.BooleanField(default=True, null=False)
    openTeacher=[
        (0, 'Pedro Mendoza Cabrera')
        (1, 'Javier Cavali Carrillo')
        (2, 'Veronica Hurtado Calcina')
    ]

    class Meta: 
        ordering = ['course_id', 'organization_id', 'course_name', 'course_status']

    def save(self, *args, **kwargs):
        self.clean()
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s" % (self.course_id, self.course_id, self.course_name, self.course_status)
