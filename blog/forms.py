from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'body', 'date', 'photo']

    # Make 'author' field read-only (disabled)
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['author'].queryset = user
            self.fields['author'].disabled = True


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
