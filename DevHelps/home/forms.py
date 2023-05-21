from .models import BlogModel
from django import  forms
from froala_editor.fields import FroalaField
from .models import BlogModel

class AddBLog(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ["content"]