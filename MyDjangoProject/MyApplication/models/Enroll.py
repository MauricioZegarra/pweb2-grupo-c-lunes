from django.db import models
import uuid

class Enroll(models.Model):
    enroll_id=models.UUIDField()
    group_id=models.ForeignKey(group_id)
    organization_id=models.ForeignKey(organization_id)
    student_id=models.ForeignKey(student_id)
    enroll_cretaed=models.DateTimeField()
    enroll_modified=models.DateTimeField()
    enroll_status=models.BooleanField()
