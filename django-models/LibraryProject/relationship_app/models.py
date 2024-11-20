from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 
# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name= 'Book')

  def __str__(self):
    return self.title

class Library(models.Model):
  name = models.CharField(max_length=150)
  books = models.ManyToManyField(Book)

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=100)
  library = models.OneToOneField(Library, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

ROLE_CHOICES = [
  ('Admin', 'Admin'),
  ('Librarian', 'Librarian'),
  ('Member', 'Member'),
]

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=10, choices=ROLE_CHOICES)

  def __str__(self):
    return self.user.username

  @receiver(post_save, sender=User)
  def create_user_profile(self, sender, instance, created, **kwargs):
    if created:
      UserProfile.objects.create(user=instance)

  @receiver(post_save, sender=User)
  def save_user_profile(self, sender, instance, **kwargs):
    instance.userprofile.save()