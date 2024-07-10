from django.db import models
from Artists.models import Artist
from Authentication.models import User
# Create your models here.

    
class Artwork(models.Model):
    MEDIUM_CHOICES = [
        ('painting', 'Painting'),
        ('sculpture', 'Sculpture'),
        ('photography', 'Photography'),
    ]
    STYLE_CHOICES = [
        ('modern', 'Modern'),
        ('expressionism', 'Expressionism'),
        ('realism', 'Realism'),
        
    ]
    GENRE_CHOICES = [
        ('landscape', 'Landscape'),
        ('portrait', 'Portrait'),
        ('conceptual', 'Conceptual'),
        ('figurative', 'Figurative'),
    ]
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='arts', null=True, blank=True, limit_choices_to={'is_artist': True})
    medium = models.CharField(max_length=100, choices=MEDIUM_CHOICES)
    year_created = models.DateField()
    image = models.ImageField(upload_to='image/', null=True)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, null=True)
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, null=True, blank=True)
    price_range_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_range_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title