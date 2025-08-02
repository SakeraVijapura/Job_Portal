from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15,null=true)
    image = models.FileField(null=true)
    gender = models.CharField(max_length=10,null=true)
    type = models.CharField(max_length=15,null=true)
    def _str_(self):
        return self.user.username

