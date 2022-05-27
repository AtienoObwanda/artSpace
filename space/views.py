from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

# View for home page
def home(request):
    return render (request, 'art/home.html')
# view for explore page
def explore(request):
    return render (request, 'art/explore.html')# view for search page
def search(request):
    return render (request, 'art/search.html')