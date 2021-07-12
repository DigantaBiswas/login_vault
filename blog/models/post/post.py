from django.db import models
from django.utils.text import slugify

from base.models import BaseAbstractModel
from blog.models import Tag


class Post(BaseAbstractModel):
    title = models.CharField(max_length=255)
    detail = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    login_url = models.URLField()
    tag = models.ManyToManyField(Tag)

    class Meta:
        app_label = "blog"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

