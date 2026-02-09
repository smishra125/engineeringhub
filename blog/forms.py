from django import forms
from .models import BlogPost, BlogComment


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'cover_image', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Write your comment..."
            })
        }
