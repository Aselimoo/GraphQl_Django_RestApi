from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at',
                    'location', 'description', 'get_image']
    list_filter = ['category', 'created_at', 'location']
    search_fields = ['title']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="200px">')
        return 'Not Image'