from django.shortcuts import render
from .models import Info
# Create your views here.

def infoo(request):
    
   
    data = Info.objects.only('phone').get(pk=1).phone
    
    return render(request,'includes/header.html',{
        'data':data
    })
    
    



 