from django import forms

class UploadFileForm(forms.Form):
    image = forms.ImageField(label='Upload an Image')
    