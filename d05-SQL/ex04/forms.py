from django import forms
from .models import Movies

class MovieRemoveForm(forms.Form):
    title = forms.ChoiceField(label="Select a movie to remove")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].choices = self.get_movie_choices()

    def get_movie_choices(self):
        try:
            movies = Movies.objects.all()
            return [(movie.title, movie.title) for movie in movies]
        except:
            return []