from django.shortcuts import render
from .models import Youtuber
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

def youtubers(request):
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()#it gives array of values.
    camera_type_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()
    tubers = Youtuber.objects.order_by('-created_date')#it gives key:value pair
    
    if request.method == "POST":
        city = request.POST.get('city')
        camera = request.POST.get('camera')
        category = request.POST.get('category')
        
        if (city and camera and category):
            tubers = tubers.filter(Q(city__icontains=city) | Q(camera_type__icontains=camera) | Q(category__icontains=category))
            
        if city:
            if (city and camera):
                tubers = tubers.filter(Q(city__icontains=city) | Q(camera_type__icontains=camera))
            elif (city and category):
                tubers = tubers.filter(Q(city__icontains=city) | Q(category__icontains=category))
            else:
                tubers = tubers.filter(city__iexact=city)
        
        if camera:
            if (camera and category):
                tubers = tubers.filter(Q(category__icontains=category) | Q(camera_type__icontains=camera))
            
            else:
                tubers = tubers.filter(camera_type__icontains=camera)
        
        if category:
            tubers = tubers.filter(category__icontains=category)                    


    return render(request,'youtubers/youtubers.html',{
        'tubers':tubers,
        'city_search':city_search,
        'camera_type_search':camera_type_search,
        'category_search' : category_search,
        
    })
        
def youtubers_details(request,id):
    tuber = get_object_or_404(Youtuber, pk=id)
    
    return render(request,'youtubers/youtuber_detail.html',{
        'tuber':tuber,
    })

def search(request):
    
    tubers = Youtuber.objects.order_by('-created_date')#it gives key:value pair
    city_search = Youtuber.objects.values_list('city',flat=True).distinct()#it gives array of values.
    camera_type_search = Youtuber.objects.values_list('camera_type',flat=True).distinct()
    category_search = Youtuber.objects.values_list('category',flat=True).distinct()
    
    
    # When we type keyword and search, its not post request its a get request because we are not 
    # storing anything on the database so its a get request
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains=keyword)#Querysets icontains is case-insensitive..
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            tubers = tubers.filter(city__iexact=city)
            
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            tubers = tubers.filter(category__iexact=city)
            
    if 'camera_type' in request.GET:
        camera_type = request.GET['camera_type']
        if camera_type:
            tubers = tubers.filter(camera_type__iexact=city)                
    
            
    return render(request, 'youtubers/search.html',{
        'tubers' : tubers,
        'city_search' : city_search,
        'camera_type_search' : camera_type_search,
        'category_search' : category_search 
    })        