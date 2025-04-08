from django.db import models
from cloudinary.models import CloudinaryField


class Painting(models.Model):
    image = models.ImageField(upload_to='static/images/gallery')
    alt_image = models.CharField(default='oil painting')
    title = models.CharField(max_length=250)
    year = models.IntegerField()

    class Meta:
        verbose_name_plural = ('paintings')
        ordering = ['-year']
