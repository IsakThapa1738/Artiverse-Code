from django.db import models
from Authentication.models import User

# Create your models here.

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist', null=True)
    name = models.CharField(max_length=255, null=True )
    biography = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='artist_profiles/', null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    social_links = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name if self.name else "Artist"