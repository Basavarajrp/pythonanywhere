from django.contrib import admin
from .models import Hiretuber
# Register your models here.

class AdminHiretubers(admin.ModelAdmin):
    list_display = ('user_id','first_name','email','tuber_name')

admin.site.register(Hiretuber,AdminHiretubers)
