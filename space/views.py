from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import *
# Create your views here.

# View for home page
def home(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render (request, 'art/home.html',{"categories": categories, "locations": locations})


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
    locations = Location.objects.all()
    categories = Category.objects.all()
    try:
        displaycategories=Image.filterByCategory(category_id)

    except Image.DoesNotExist:
        raise Http404()
    return render(request, 'art/category.html', {"categories": categories, "locations": locations, "displaycategories":displaycategories})

def imageLocation(request, location_id):
    locations = Location.objects.all()
    categories = Category.objects.all()
    try:
        displaylocations=Image.filterByLocation(location_id)

    except Image.DoesNotExist:
        raise Http404()
    return render(request,'art/location.html', {"categories": categories, "locations": locations,"displaylocations": displaylocations}) 



def search(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.searchImage(search_term)
        message=f'{search_term}'
    return render (request, 'art/search.html',{"message":message,"images": searched_images, "categories": categories, "locations": locations})