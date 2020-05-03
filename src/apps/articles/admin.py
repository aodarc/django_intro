from django.contrib import admin

# Register your models here.
from apps.articles.models import Article, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'body', 'author__email')
    ordering = ('-created_at',)
