from django import forms


class TriangleForm(forms.Form):
    size_a = forms.IntegerField(required=True, min_value=1, max_value=1000)
    size_b = forms.IntegerField(required=True, min_value=1, max_value=1000)
