from django import forms
from .models import Blog_comment


class Blog_commentForm(forms.ModelForm):

    class Meta:
        model = Blog_comment
        fields = ('text',)
