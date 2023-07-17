from django.db import models
from . import User_Type
import uuid

class User(models.Models):
    user_id = models.UUIDField()
    user_type_id = models.ForeignKey(User_Type, related_name="user_type_id", to_field = 'user_type_id')
    user_dni = models.IntegerField()
    user_dob = models.DateField()
    user_email = models.EmailField()
    user_last_name = models.CharField()
    user_name = models.CharField()
    user_password = models.CharField()
    user_promedio = models.IntegerField()
    user_puesto = models.IntegerField()

    class Meta: 
        ordering = ['user_name', 'user_id', 'user_type_id', 'user_dni', 'user_email', 'user_promedio', 'user_puesto']

    def save(self, *args, **kwargs):
        self.clean()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (self.user_id, self.user_type_id, self.user_dni, self.user_dob, self.user_email, self.user_last_name, self.user_name, self.user_passwqrd, self.user_promedio, self.user_puesto)
