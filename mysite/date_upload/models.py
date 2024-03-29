from django.db import models
from django.contrib.auth.models import User

class Raw_data(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    csv = models.FileField(upload_to='csv/')

    def __str__(self):
        return self.name

class UserProfileInfo (models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username