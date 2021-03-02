from django.db import models

# Create your models here.


class Hiretuber(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True,auto_now_add=True)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email