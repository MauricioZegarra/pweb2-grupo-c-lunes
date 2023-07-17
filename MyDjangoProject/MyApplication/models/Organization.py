from django.db import models
from . import Organization
import uuid

class Organization(models.Models):
    
    organization_id = models.ForeignKey(Organization, related_name='organization_id', tofield = 'organization_id')
    organization_name = models.CharField(null=False, blank=False, max_length=255)
    organization_status = models.BooleanField(default=True, null=False)
    class Meta: 
        ordering = [  'organization_id', 'organization_name', 'organization_status']

    def save(self, *args, **kwargs):
        self.clean()
        return super(Organization, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s" % (self.organization_id, self.organization_name,self.organization_status)
