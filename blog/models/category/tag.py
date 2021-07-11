from django.db import models

from base.models import BaseAbstractModel


class Tag(BaseAbstractModel):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = "blog"

    def __str__(self):
        return self.name