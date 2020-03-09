from .models import User
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('profile_image',)