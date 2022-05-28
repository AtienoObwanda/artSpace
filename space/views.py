from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
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
    try:
        categories=Image.filterByCategory(category_id)

    except Image.DoesNotExist:
        raise Http404()
    return render(request, 'art/category.html', {'categories': categories})

def imageLocation(request, location_id):
    try:
        locations=Image.filterByLocation(location_id)

    except Image.DoesNotExist:
        raise Http404()
    return render(request,'art/location.html', {'locations': locations}) 



def search(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.searchImage(search_term)
        message=f'{search_term}'
    return render (request, 'art/search.html',{"message":message,"images": searched_images})