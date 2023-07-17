from django.db import models
from . import Organization
import uuid

class School(models.Models):
    school_id = models.UUIDField()
    organization_id = models.ForeignKey(Organization, related_name='organization_id', tofield = 'organization_id')
    school_name = models.CharField()
    school_status = models.BooleanField()

    class Meta: 
        ordering = ['school_id', 'organization_id', 'school_name', 'school_status']

    def save(self, *args, **kwargs):
        self.clean()
        return super(School, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s" % (self.school_id, self.organization_id, self.school_name, self.school_status)
