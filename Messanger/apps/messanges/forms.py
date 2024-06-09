from django import forms
from .models import MediaFile

class MediaFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'image', 'video', 'audio', 'Chat_id', 'Sender_id']

class ImageFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'image', 'Chat_id', 'Sender_id']

class VideoFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'video', 'Chat_id', 'Sender_id']

class AudioFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'audio', 'Chat_id', 'Sender_id']