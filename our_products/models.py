from django.db import models
from django.contrib.auth.models import User


class OurProduct(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('software', 'Software'),
        ('hardware', 'Hardware'),
    ]

    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES)

    preview_image = models.ImageField(upload_to='our_products/previews/', blank=True, null=True)
    file = models.FileField(upload_to='our_products/files/', blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def likes_count(self):
        return self.likes.count()   # uses ProductLike

    def __str__(self):
        return self.title


class ProductLike(models.Model):
    product = models.ForeignKey(OurProduct, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("product", "user")

class ProductComment(models.Model):
    product = models.ForeignKey(
        OurProduct,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} on {self.product}"
