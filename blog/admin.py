from django.contrib import admin
from .models import Article, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'is_published']
    list_filter = ['is_published', 'published_date', 'tags']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    filter_horizontal = ['tags']
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'slug', 'content')
        }),
        ('Налаштування', {
            'fields': ('tags', 'is_published', 'published_date')
        }),
    )
