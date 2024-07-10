from django import forms
from .models import Artist
import json

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'biography', 'profile_picture', 'contact_email', 'contact_phone', 'website', 'social_links']
        
def clean_social_links(self):
        data = self.cleaned_data.get('social_links')
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                raise forms.ValidationError("Invalid JSON format")
        return data