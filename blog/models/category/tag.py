from django.db import models

from base.models import BaseAbstractModel
from blog.utills.unique_slug_generator import unique_slugify


class Tag(BaseAbstractModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        app_label = "blog"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug_str = self.name
        unique_slugify(self, slug_str)
        super().save(*args, **kwargs)
