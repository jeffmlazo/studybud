from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(
        null=True, blank=True)  # This field can't be blank
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    # Takes a snapshot everytime the model is called
    updated = models.DateTimeField(auto_now=True)
    # Takes a snapshot once only or if this instance is created in initial
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # The '-' will order the latest updated or created post from the database
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # The '-' will order the latest updated or created post from the database
        ordering = ['-updated', '-created']

    def __str__(self):
        # This means that the value will return only 50 characters
        return self.body[0:50]
