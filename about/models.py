from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class Event(models.Model):
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    

    def __str__(self):
        return self.description
   
