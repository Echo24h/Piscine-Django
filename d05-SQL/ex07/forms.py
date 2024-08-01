from django import forms
from ex07.models import Movies

class MovieUpdateForm(forms.ModelForm):
    title = forms.ChoiceField(label="Select Movie")
    opening_crawl = forms.CharField(widget=forms.Textarea, label="Opening Crawl")

    class Meta:
        model = Movies
        fields = ['opening_crawl']  # Spécifiez uniquement les champs que vous voulez modifier

    def __init__(self, *args, **kwargs):
        # Inclure l'instance de modèle pour pré-remplir le champ title
        movie_choices = [(movie.title, movie.title) for movie in Movies.objects.all()]
        super().__init__(*args, **kwargs)
        self.fields['title'] = forms.ChoiceField(choices=movie_choices, label="Select Movie")