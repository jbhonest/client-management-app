from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    profile_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
