from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    published_date = models.DateField(null=True, blank=True)
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title
    
class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library,on_delete=models.CASCADE)
class UserProfile(models.Model):
    USER_CHOICES = [
        ('Admin' , 'Admin'),
        ('Librarian' , 'Librarian'),
        ('Member' , 'Member'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    role = models.CharField(max_length=15,choices=USER_CHOICES,default='MB')
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        instance.userprofile.save()