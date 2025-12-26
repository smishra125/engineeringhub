from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    category = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
