from django import forms

class SubmissionForm(forms.Form):
    text = forms.CharField(label='Your Text', max_length=100)