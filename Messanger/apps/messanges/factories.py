from .forms import MediaFileForm, ImageFileForm, VideoFileForm, AudioFileForm

class FormFactory:
    @staticmethod
    def get_form(file_type):
        if file_type == 'image':
            return ImageFileForm
        elif file_type == 'video':
            return VideoFileForm
        elif file_type == 'audio':
            return AudioFileForm
        else:
            return MediaFileForm
