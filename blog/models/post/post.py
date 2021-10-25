from django.db import models
from django.utils.text import slugify

from base.models import BaseAbstractModel
from blog.models import Tag
from blog.utills.unique_slug_generator import unique_slugify


class Post(BaseAbstractModel):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    login_url = models.URLField()
    image_url = models.URLField(blank=True, null=True)
    tag = models.ManyToManyField(Tag)

    class Meta:
        app_label = "blog"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        slug_str = self.title
        unique_slugify(self, slug_str)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return self.slug
