from django import forms
from .models import Artwork

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'medium','style','genre', 'year_created', 'image', 'description', 'price']
        widgets = {
            'medium': forms.Select(choices=[( ('Painting', 'Painting'),'Sculpture', 'Sculpture'), ('Photography', 'Photography')]),
            'style':forms.Select(choices=[(('Modern', 'Modern'),('Expressionism', 'Expressionism'),('Realism', 'Realism'),)]),
            'genre':forms.Select(choices=[(('Landscape', 'Landscape'),('Portrait', 'Portrait'),('Conceptual', 'Conceptual'),('Figurative', 'Figurative'),)]),
            
        }
