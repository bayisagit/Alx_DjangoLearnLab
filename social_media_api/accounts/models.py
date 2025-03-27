from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
   # Many-to-many relationship for followers (users who follow this user)
    followers = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    
    # Many-to-many relationship for following (users this user is following)
    following = models.ManyToManyField('self', related_name='following_users', symmetrical=False, blank=True)

    def __str__(self):
        return self.username