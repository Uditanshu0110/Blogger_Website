from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
class Post(models.Model):
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200,null=True)
    image = models.FileField(null=True)
    date = models.DateField(null=True)
    short_des = models.TextField(null=True)
    long_des = models.TextField(null=True)

    def __str__(self):
        return self.title + '--' +self.cat.name +'--'+self.usr.username

class PostLike(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post_data = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.post_data.title +'--'+self.usr.username

class PostComment(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_data = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.TextField(null=True)
    date = models.DateField(null=True)
    def __str__(self):
        return self.post_data.title + '--' + self.usr.username


class UserDetail(models.Model):
    usr = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.FileField(null=True)

