from django import forms
from .models import People

class SearchForm(forms.Form):
    min_release_date = forms.DateField(label="Movies minimum release date", widget=forms.DateInput(attrs={'type': 'date'}))
    max_release_date = forms.DateField(label="Movies maximum release date", widget=forms.DateInput(attrs={'type': 'date'}))
    min_planet_diameter = forms.IntegerField(label="Planet diameter greater than")
    character_gender = forms.ChoiceField(label="Character gender", choices=[(gender, gender) for gender in People.objects.values_list('gender', flat=True).distinct()])