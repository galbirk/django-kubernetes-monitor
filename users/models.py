from django.db import models
from django.contrib.auth.models import User

class User_Role(models.Model):
    role = models.CharField(max_length=20,default='client')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.role