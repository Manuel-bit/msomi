from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200, null=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=200, null=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'