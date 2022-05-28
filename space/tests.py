from django.test import TestCase
from .models import *
# Create your tests here.
# Image Test
class ImageTest(TestCase):
    def setUp(self):
        self.new_category = Category(name='Food')
        self.new_category.save()

        self.new_location = Location(name='Kenya')
        self.new_location.save()

        self.new_tag = Tags(name = 'testing')
        self.new_tag.save()

        self.new_image=Image(image_name='food',image_description='Chinese Delicacy')
        self.new_image.save_image() 

        self.new_image.Category.add(self.new_category)
        self.new_image.Location.add(self.new_location)
        self.new_image.Tags.add(self.new_tag)

        # def tearDown(self):
        # Image.objects.all().delete()
        # tags.objects.all().delete()
        # Article.objects.all().delete()

