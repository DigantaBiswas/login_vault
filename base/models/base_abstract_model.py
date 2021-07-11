from datetime import datetime, timezone

from django.db import models

# Create your models here.
class BaseAbstractModel(models.Model):
    """
    This model is an abstract model
    This model contains basic fields for all other models.
    This model will be designed as a parent model for every other models
    """
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(default=datetime.now())
    # is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        app_label = "base"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = datetime.now(tz=timezone.utc)
        self.updated_at = datetime.now(tz=timezone.utc)
        return super(BaseAbstractModel, self).save(*args, **kwargs)