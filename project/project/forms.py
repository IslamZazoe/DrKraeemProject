from django import forms

class InputForm(forms.Form):
    x = forms.IntegerField(label="first value")
    y = forms.IntegerField(label="second value")