from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Image
# Create your views here.

# View for home page
def home(request):
    return render (request, 'art/home.html')
# view for explore page
def explore(request):
    images = Image

    return render (request, 'art/explore.html', {"images":images})# view for search page
def search(request):
    return render (request, 'art/search.html')