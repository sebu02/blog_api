from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255,unique=True)
    
    def __str__(self):
        return str(self.username)
    
    
class BlogPost(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    content=models.TextField(max_length=255,null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now,blank=True,null=True)
   
    def __str__(self):
        return str(self.id)
    
    
class Comment(models.Model):
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    content=models.TextField(max_length=200,blank=True,null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(default=timezone.now,blank=True,null=True)

    def __str__(self):
        return str(self.id)