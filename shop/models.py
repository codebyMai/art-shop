from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    CATEGORY_CHOICES = (
        ('La', 'Landscape'),
        ('Se', 'Seascape'),
        ('St', 'Still life'),
        ('Fl', 'Flowers'),
    )
    category = models.CharField(choices=CATEGORY_CHOICES)
    posted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
