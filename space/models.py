from django.db import models
from django_resized import ResizedImageField


# Models created are: image,category,location, and user

# class User(models.Model):
#     firstName = models.CharField(max_length=30)
#     lastName = models.CharField(max_length=30)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length = 10,blank =True)

# Category model
class Category(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

# Location model
class Location(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

# Tags model
class Tags(models.Model):
    name = models.CharField()
    def __str__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/', blank=True)
    imageName = models.CharField(max_length=60)
    description = models.TextField()
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags= models.ManyToManyField(Tags)

    def __str__(self):
        return self.imageName
