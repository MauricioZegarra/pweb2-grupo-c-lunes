from django.db import models
import uuid

class Group(models.Model):
    group_id = models.UUIDField()
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group_created = models.DateTimeField()
    group_modified = models.DateTimeField()
    group_name = models.CharField(max_length=255)
    group_status = models.BooleanField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['group_id', 'group_created', 'group_modified']
    
    def save(self, *args, **kwargs):
        self.group_name = self.group_name.upper()
        return super(Group, self).save(*args, **kwargs)
    
    def __str__(self):
        return "%s %s %s %s" % (self.group_id, self.assignment_id, self.organization_id, self.teacher_id)
