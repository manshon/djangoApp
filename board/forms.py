from django import forms
from .models import Board, Comment


class BoardCreateForm(forms.ModelForm):
    # tag = forms.CharField(label='タグ', max_length=30)

    class Meta:
        model = Board
        fields = (
            'title',
            'body',
            'tag',
        )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = (
            'body',
        )