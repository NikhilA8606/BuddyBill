from uuid import uuid4

from django.db import models

# Create your models here.
class BaseManager(models.Manager):
    pass

class BaseModel(models.Model):
    external_id = models.UUIDField(db_index=True, default=uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BaseManager()

    class Meta:
        abstract = True
