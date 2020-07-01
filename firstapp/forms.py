from django import forms
  
class UserForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100)
    age = forms.IntegerField(required=False, min_value=18, max_value=100)