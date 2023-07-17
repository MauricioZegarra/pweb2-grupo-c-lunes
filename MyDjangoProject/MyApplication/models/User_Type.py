from django.contrib import models
import UUID

class User_Tyoe(models.Models):
    user_type_id = models.UUIDField()
    user_type_name = models.CharField()
    user_type_status = models.BooleanField()

    class Meta: 
        ordering = ['user_type_id', 'user_type_name', 'user_type_status']

    def save(self, *args, **kwargs):
        self.clean()
        return super(User_Type, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s" % (self.user_type_id, self.user_type_name, self.type_status)
