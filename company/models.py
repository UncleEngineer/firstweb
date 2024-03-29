from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=160)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProductDemo(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    price = models.FloatField(default=1)
    instock = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '-' + str(self.price)