from django.db import models

class Raw_data(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    csv = models.FileField(upload_to='csv/')

    def __str__(self):
        return self.name
