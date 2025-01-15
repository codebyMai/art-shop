from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    image = models.ImageField(upload_to = 'static/images', null=True)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    SUBJECT_CHOICES = (
        ('La', 'Landscape'),
        ('Se', 'Seascape'),
        ('St', 'Still life'),
        ('Fl', 'Flowers'),
    )
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    added = models.DateTimeField(auto_now_add=True)
    is_miniature=models.BooleanField(default=False)
    is_featured=models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_miniature']

    def __str__(self):
        return self.title
