from django.db import models
from apps.core.models import TimeBase


class Ideas(TimeBase):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()

    class Meta:
        db_table = 'ideas'

    def __str__(self):
        return self.name


class ReplyToIdea(TimeBase):
    idea = models.ForeignKey(Ideas, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()


class IdeasImages(TimeBase):
    repliedidea = models.ForeignKey(ReplyToIdea, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='replied_images/')

    class Meta:
        db_table = 'ideasimages'

    def __str__(self):
        return self.repliedidea

    