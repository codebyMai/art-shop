from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    image = models.ImageField(upload_to = 'images/products', null=True)
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
    TYPE_CHOICES = (
        ('Mi', 'Miniature'),
        ('Pa', 'Painting'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)

    class Meta:
        ordering = ['-added']

    def __str__(self):
        return self.title


