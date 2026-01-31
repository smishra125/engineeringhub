from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='blog/')
    content = models.TextField()

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
