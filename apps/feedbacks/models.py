from django.db import models
from apps.core.models import TimeBase


class Feedbacks(TimeBase):
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email_or_number = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    read = models.BooleanField(default=False)

    class Meta:
        db_table = 'feedback'

    def __str__(self):
        return self.body
