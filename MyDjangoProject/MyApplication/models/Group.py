from django.db import models
import uuid

class Group(models.Model):
    group_id=models.UUIDField()
    assignment_id=models.ForeignKey(assignment_id)
    organization_id=models.ForeignKey(organization_id)
    teacher_id=models.ForeignKey(teacher_id)
    group_cretaed=models.DateTimeField()
    group_modified=models.DateTimeField()
    group_name=models.CharField()
    group_status=models.BooleanField()
    
    def save(self, *args, **kwargs):
        self.names = self.names.upper()
        self.father_surname = self.father_surname.upper()
        self.mother_surname = self.mother_surname.upper()
        return super(Student, self).save(*args, **kwargs)
    
    def __str__(self):
        return " %s %s %s %s" % (self.cui, self.names, self.father_surname,self.mother_surname)