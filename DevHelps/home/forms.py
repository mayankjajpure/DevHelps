from .models import BlogModel
from django import  forms
from froala_editor.fields import FroalaField


class AddBLog(forms.Form):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = forms.CharField(label="Heading", max_length=100)
    content =  FroalaField()
    slug = forms.SlugField(max_length=100)
    image = forms.ImageField()
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()