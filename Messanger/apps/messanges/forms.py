from django import forms
from .models import MediaFile

class MediaFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'image', 'video', 'audio']

class ImageFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'image']

class VideoFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'video']

class AudioFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'audio']
