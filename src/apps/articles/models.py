from django.conf import settings
from django.db import models


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)


class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=255, verbose_name='Title', db_index=True)
    body = models.TextField(max_length=5000, verbose_name='Article body')
    tags = models.ManyToManyField(to='Tag', related_name='articles', blank=True)
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='articles'
    )
