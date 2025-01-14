from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    SUBJECT_CHOICES = (
        ('Or', 'Order'),
        ('Re', 'Return'),
        ('Co', 'Commission'),
        ('Ot', 'Other'),
    )
    subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fname
