from django.db import models
from cloudinary.models import CloudinaryField

class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title