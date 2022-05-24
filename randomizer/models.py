from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel


class RandomizedNumber(TimeStampedModel):
    value = models.IntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
