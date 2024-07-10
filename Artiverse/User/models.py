from django.db import models
from Authentication.models import User
from Artworks . models import Artwork
# Create your models here.
class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    name = models.CharField(max_length=255, null=True)
    biography = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='user_profiles/', null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class BillingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='billing_address', null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    zip_code = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Billing Address"

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'artwork')  # Ensure each artwork can only be wishlisted once per user
    
    def __str__(self):
        return f"{self.user.username}'s Wishlist"