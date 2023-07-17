from django.db import models
import uuid

class Assignment(models.Model):
    assignment_id = models.UUIDField()
    academic_id = models.ForeignKey(Academic, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    assignment_created = models.DateTimeField()
    assignment_modified = models.DateTimeField()
    assignment_status = models.BooleanField()

    class Meta:
        ordering = ['assignment_id', 'assignment_created', 'assignment_modified']
    
    def __str__(self):
        return "%s %s %s %s" % (self.assignment_id, self.academic_id, self.course_id, self.teacher_id)
