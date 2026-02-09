from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

    

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='blog/')
    content = CKEditor5Field('Content', config_name='default')

    author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="blog_posts",
    null=True,
    blank=True
)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} on {self.post}"