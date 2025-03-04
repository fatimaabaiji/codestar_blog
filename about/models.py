from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class AboutEvent(models.Model):
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    class Meta:
        db_table = 'about_event'  # Specify the custom table name

    def __str__(self):
        return self.description
    
class Event(models.Model):
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    class Meta:
        db_table = 'blog_event'

    def __str__(self):
        return self.title


