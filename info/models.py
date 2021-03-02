from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    insta = models.CharField(max_length=255)
    fb = models.CharField(max_length=255)
    tweeter = models.CharField(max_length=255)
    youtube = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name