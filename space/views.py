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

def search(request):
    return render (request, 'art/search.html')