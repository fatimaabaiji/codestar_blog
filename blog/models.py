from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey( User, on_delete=models.CASCADE, related_name='blog_posts' )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(default=timezone.now)
    


    class Meta:
        pass

    def __str__(self):
        return f"Post: {self.title} by {self.author}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)  
    challenge = models.FloatField(default=3.0)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


class Event(models.Model):
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    class Meta:
        db_table = 'blog_event'


     

    def __str__(self):
        return self.title

