import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='host')
    members = models.ManyToManyField(User, related_name='members')
    name = models.CharField(max_length=255)
    description = models.TextField()
    public = models.BooleanField(default=True)
    code_to_join = models.CharField(max_length=255, null=True, blank=True)
    poster = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Avatar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='id_user')
    # avatar = models.ForeignKey(Avatar, on_delete=models.CASCADE, related_name='avatar')
    points = models.IntegerField(default=0)
    bio = models.TextField()
    gender = models.CharField(max_length=255, null=True, blank=True)
    day_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

# class Post(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     id_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='id_room')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')
#     date = models.DateTimeField(auto_now_add=True)
#     text = models.TextField()
#     status = models.CharField(max_length=255, null=True, blank=True)

# class Reply(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     id_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='id_post')
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_reply')
#     date = models.DateTimeField(auto_now_add=True)
#     text = models.TextField()
#     status = models.CharField(max_length=255, null=True, blank=True)

