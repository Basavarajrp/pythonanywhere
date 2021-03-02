from django.contrib import admin
from .models import Slider,Team,Aboutproject
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    
    
    # These all fields are comming from model inlines..(ModelAdmin.inlines)
    list_display = ('id','myphoto','first_name','role','created_date') #fields to be displayed on admin pannel.
    list_display_links = ('first_name',) #enabling name to click 
    search_fields = ('first_name','role') # search field on top
    list_filter = ('role',) #filter based on roles on right side

class AdminSlider(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    
    list_display = ('headline','myphoto','button_text')
    
    
    
admin.site.register(Slider,AdminSlider)
admin.site.register(Team,TeamAdmin)
admin.site.register(Aboutproject)