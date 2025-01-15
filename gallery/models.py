from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Painting(models.Model):
    image = models.ImageField(upload_to='static/images/gallery')
    title = models.CharField(max_length=250)
    year = models.IntegerField()
    
    class Meta:
        verbose_name_plural = ('paintings')
        ordering = ['-year']
