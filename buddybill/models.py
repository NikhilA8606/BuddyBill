from django.db import models


class Group(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
    )
    description = models.TextField(
        null=False,
    )
