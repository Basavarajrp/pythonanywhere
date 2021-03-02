from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    subject = models.CharField(max_length=255) 
    message = models.TextField(blank=True) 
    
    def __str__(self):
        return self.email