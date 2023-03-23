from django.contrib import admin
from .models import BlogCategory, BlogTag, Post


# Register your models here.
@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
       list_display = [
        'title',
        'id',
        'is_active',
    ]

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
       list_display = [
        'title',
        'id',
        'is_active',
    ]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id',
        'is_active',
    ]

