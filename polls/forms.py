from django import forms
from django.forms import ModelForm

from .models import Person


class TriangleForm(forms.Form):
    size_a = forms.IntegerField(required=True, min_value=1, max_value=1000)
    size_b = forms.IntegerField(required=True, min_value=1, max_value=1000)


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
