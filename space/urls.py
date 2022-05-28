from django import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    # path('', admin.site.urls),
    path('', views.home, name='home'),
    path('explore', views.explore, name='explore'),
    path('search', views.search, name='search')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)