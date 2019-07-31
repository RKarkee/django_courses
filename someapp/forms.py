from django import forms
from someapp import models

class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comments
        fields=[]



