from django.db import models
from django.contrib.auth.models import User
# Create your models here.

"""
    The model for a blog post 
"""


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
