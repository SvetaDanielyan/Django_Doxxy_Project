from django import forms
from news.models import Comments


class CommentForm(forms.ModelForm):
    comment = forms.CharField(min_length=3, max_length=699)
    slug = forms.CharField(min_length=3, max_length=699)

    class Meta:
        model = Comments
        fields = ('comment', 'slug')