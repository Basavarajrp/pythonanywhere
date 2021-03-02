from django.shortcuts import render
from .models import Slider,Team,Aboutproject
from youtubers.models import Youtuber
# Create your views here.


def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    youtubers = Youtuber.objects.all()
    return render(request,'webpages/home.html',{
        'sliders' : sliders,
        'teams' : teams,
        'featured_youtubers' : featured_youtubers,
        'youtubers':youtubers,
    })  

def about(request):
    
    team = Team.objects.all()
    dis = Aboutproject.objects.all()
    
    return render(request, 'webpages/about.html',{
        'team':team,
        'dis' : dis,
    })

def contact(request):
    
    return render(request, 'webpages/contact.html')

def services(request):
    
    return render(request,'webpages/services.html')