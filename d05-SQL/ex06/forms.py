from django import forms

class MovieUpdateForm(forms.Form):
    title = forms.ChoiceField(label="Select Movie")
    opening_crawl = forms.CharField(widget=forms.Textarea, label="Opening Crawl")