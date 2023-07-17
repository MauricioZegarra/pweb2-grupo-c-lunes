from django.db import models
import uuid

class Enroll(models.Model):
    enroll_id = models.UUIDField()
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    enroll_created = models.DateTimeField()
    enroll_modified = models.DateTimeField()
    enroll_status = models.BooleanField()

    class Meta:
        ordering = ['enroll_id', 'enroll_created', 'enroll_modified']

    def __str__(self):
        return "%s %s %s %s" % (self.enroll_id, self.group_id, self.organization_id, self.student_id)
