from django.contrib import admin

# Register your models here.
from apps.blogusers.models import BlogUser


@admin.register(BlogUser)
class BlogUserAdmin(admin.ModelAdmin):
    pass
