from django.db import models
from . import Organization
import uuid

class Semester(models.Models):
    semester_id = models.UUIDField()
    organization_id = models.ForeignKey(Organization, related_name='organization_id', tofield = 'organization_id')
    semester_name = models.CharField()
    semester_status = models.BooleanField()

    class Meta: 
        ordering = ['semester_id', 'organization_id', 'semester_name', 'semester_status']

    def save(self, *args, **kwargs):
        self.clean()
        return super(Semester, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s" % (self.semester_id, self.organization_id, self.semester_name, self.semester_status)
