from django import views
from django.urls import path
from .import views
urlpatterns = [
    # path('', admin.site.urls),
    path('', views.home, name='home'),
    path('explore', views.explore, name='explore'),
    path('search', views.search, name='search')

]