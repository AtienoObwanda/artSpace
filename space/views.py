from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

# View for home page
def home(request):
    return HttpResponse('Home')

# view for explore page
def explore(request):
    return HttpResponse('Explore')
# view for search page
def search(request):
    return HttpResponse('Search')