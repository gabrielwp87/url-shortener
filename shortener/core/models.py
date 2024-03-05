from django.db import models

# Create your models here.


class UrlRedirect(models.Model):
    destiny = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True)
    created_in = models.DateTimeField(auto_now_add=True)
    updated_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'UrlRedirect to: {self.destiny}'

