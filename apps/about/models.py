from django.db import models
from apps.core.models import TimeBase
from googletrans import Translator


class About(TimeBase):
    title = models.CharField(max_length=100)
    title_uz = models.CharField(max_length=100, blank=True, null=True)
    title_ru = models.CharField(max_length=100, blank=True, null=True)

    body = models.TextField(null=True, blank=True)
    body_uz = models.TextField(null=True, blank=True)
    body_ru = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to='about_images/', blank=True, null=True)
    about_image = models.CharField(max_length=255, null=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'about'
        ordering = ['order']

    def save(self, *args, **kwargs):
        translator = Translator()

        if not self.title_ru:
            self.title_ru = translator.translate(self.title, dest='ru').text
        if not self.title_uz:
            self.title_uz = translator.translate(self.title, dest='uz').text

        if not self.body_ru:
            self.body_ru = translator.translate(self.body, dest='ru').text
        if not self.body_uz:
            self.body_uz = translator.translate(self.body, dest='uz').text

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
