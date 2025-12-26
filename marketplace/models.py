from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to='products/')
    affiliate_link = models.URLField()

    def __str__(self):
        return self.title
