from django import forms
from .models import clip

class ClipPostForm(forms.ModelForm):
    clipID = forms.CharField(max_length=300)
    contents = forms.CharField(label='', widget=forms.Textarea)


    class Meta:
        model = clip
        fields = ['clipID', 'contents']
