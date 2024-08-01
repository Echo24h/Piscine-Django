from django import forms
from .models import Movies

class MovieRemoveForm(forms.Form):
    title = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].choices = [(movie.title, movie.title) for movie in Movies.objects.all()]