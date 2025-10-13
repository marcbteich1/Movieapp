from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['MovieID','MovieTitle','Actor1Name','Actor2Name','DirectorName','MovieGenre','ReleaseYear']

class LookupForm(forms.Form):
    MovieID = forms.IntegerField()