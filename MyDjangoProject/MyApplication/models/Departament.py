from django.db import models
from . import Organization
import uuid

class Organization(models.Models):
    departament_id= models.CharField(unique=True, null=True, blank=True, max_length=25)
    organization_id = models.ForeignKey(Organization, related_name='organization_id', tofield = 'organization_id')
    departament_name = models.CharField(null=False, blank=False, max_length=255)
    departament_status = models.BooleanField(default=True, null=False)
    class Meta: 
        ordering = [  'departament_id', 'departament_name', 'departament_status']

    def save(self, *args, **kwargs):
        self.clean()
        return super(Organization, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s" % (self.departament_id,self.organization_id, self.departament_name, self.departament_status)
