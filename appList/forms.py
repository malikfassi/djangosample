from django import forms
from .models import Application

class UploadForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['description', 'url', 'zipFile', 'access']