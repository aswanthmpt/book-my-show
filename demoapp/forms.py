from .models import Movie
from django import forms
from django.forms import TextInput
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
       
        # fields=['name','rating','type','language','certificate','category','duration','date','poster','banner'] 
        fields='__all__'
        widgets = {
            'name': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'Name'}),
            'rating': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'rating'}),
            'type': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'type'}),
            'language': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'language'}),
            'category': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'category'}),
            'duration': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'duration'}),
            'certificate': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'certificate'}),
            'date': TextInput(attrs={'class': "form-control",'style': 'max-width: 300px;','placeholder': 'date'}),
            }