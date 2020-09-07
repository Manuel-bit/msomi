from django.db import models


# Create your models here.

class Courses(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=False)
    

