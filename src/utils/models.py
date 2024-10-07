import uuid

from django.db import models

__all__ = [
    "UUIDModel",
    "TimestampModel",
    "BaseModel",
]


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimestampModel):
    class Meta:
        abstract = True
