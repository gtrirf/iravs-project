from django.db import models
from apps.core.models import TimeBase
from django.contrib import messages
from django.core.exceptions import ValidationError


class MainPage(TimeBase):
    image = models.ImageField(upload_to='main_page/', null=True, blank=True)
    full_name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        db_table = 'main_page'

    def clean(self):
        if not self.pk and MainPage.objects.exists():
            raise ValidationError("Only one MainPage instance is allowed.")

    def __str__(self):
        return self.full_name


class Socials(TimeBase):
    social_name = models.CharField(max_length=255)
    social_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'socials_links'

    def __str__(self):
        return self.social_name

