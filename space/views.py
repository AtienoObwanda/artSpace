from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.

# View for home page
def home(request):
    return render (request, 'art/home.html')


# view for explore page
def explore(request):
    # images = Image.objects.all()
    images = Image.getImages()
    locations = Location.objects.all()
    categories = Category.objects.all()

    # context = {}
    # context['images'] = images

    return render (request, 'art/explore.html', {"images": images, "categories": categories, "locations": locations})# view for search page

def imageCategory(request, category_id):
    images = Image.filterByCategory(category_id) 
    return render(request,'art/category.html',{"images":images}) 

def imageLocation(request, location_id):
    images = Image.filterByLocation(location_id) 
    return render(request,'art/location.html',{"images":images}) 



def search(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.searchImage(search_term)
        message=f'{search_term}'
    return render (request, 'art/search.html',{"message":message,"images": searched_images})