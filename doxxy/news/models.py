from django.db import models
from datetime import datetime


class Languages(models.TextChoices):
    en = 'en'
    de = 'de'
    fr = 'fr'


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, default='', blank=False)
    description = models.CharField(max_length=5000, default='', blank=False, help_text='News content')
    slug = models.SlugField(unique=True, blank=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name_plural = '📰 News'


class Comments(models.Model):
    news_slug = models.ForeignKey(News, on_delete=models.CASCADE, default='')
    comment = models.CharField(max_length=150, default='', blank=False)
    language = models.CharField(
        max_length=2,
        choices=Languages.choices,
        default=Languages.en,
    )
    created_at = models.DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
       super(Comments, self).save(*args, **kwargs)

    def __str__(self):
        return f'news_slug: {self.news_slug} | comment: {self.comment}'

    class Meta:
        verbose_name_plural = '💬 Comments'
