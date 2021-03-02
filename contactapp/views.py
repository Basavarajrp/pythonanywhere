from django.shortcuts import render, redirect
from .models import Contact
# Create your views here.


def teamcontact(request):
    
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']
        
        contacts = Contact(name=name,phone=phone,email=email,
                           company=company,subject=subject,message=message)
        
        contacts.save()
        
        return redirect('youtubers')
    