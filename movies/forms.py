from django import forms
from .models import Genre,Movie,Score

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'