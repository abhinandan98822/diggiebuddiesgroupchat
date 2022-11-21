from django import forms
  
class ImageForm(forms.Form):
    file_field = forms.FileField()