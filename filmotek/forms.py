from django import forms
from django.forms import fields
from .models import Film, Realisator

class RealisatorForm(forms.ModelForm):
    # name = forms.CharField(label="Nom du Réalisateur", max_length=350)
    class Meta:
        model = Realisator
        fields = '__all__'
    pass

class FilmForm(forms.ModelForm):
    # vote = forms.IntegerField(min_value=0, max_value=10)
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'})
        }